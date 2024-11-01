import csv
import functools
import json
import logging
from collections import namedtuple
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from openai import AsyncOpenAI, OpenAIError
from tqdm.asyncio import tqdm

load_dotenv()
logging.basicConfig(level=logging.INFO)

Question = namedtuple('Question', ['id', 'slug', 'category', 'title', 'link'])
Result = namedtuple('Result', ['id', 'slug', 'category', 'title', 'link', 'answer'])


@asynccontextmanager
async def async_open_file(path, mode):
    f = open(path, mode, newline='', buffering=1)  # buffering=1 for line buffering
    try:
        yield f
    finally:
        f.close()


@functools.lru_cache()
def load_prompt():
    with open('prompt.json') as f:
        return json.load(f)


async def write_result_to_csv(result, output_path):
    async with async_open_file(output_path, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(result)


def get_questions(input_path):
    questions = []
    with open(input_path) as csvfile:
        fieldnames = ['id', 'slug', 'category', 'title', 'state', 'answers_count', 'link']
        rows = csv.DictReader(csvfile, delimiter=';', fieldnames=fieldnames)
        next(rows)
        for row in rows:
            title = row['title'].strip()
            question = Question(row['id'], row['slug'], row['category'], title, row['link'])
            questions.append(question)
    return questions


async def get_answers_and_write(questions, output_path):
    with open(output_path, 'a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:  # Check if file is empty to write headers
            writer.writerow(['id', 'slug', 'category', 'title', 'link', 'answer'])

    tasks = [process_question(question, output_path) for question in questions]
    await tqdm.gather(*tasks)


async def process_question(question, output_path):
    answer = await get_answer(question.title)
    r = (
        question.id,
        question.slug,
        question.category,
        question.title,
        question.link,
        answer
    )
    await write_result_to_csv(r, output_path)


client = AsyncOpenAI()


async def get_answer(question):
    logging.info(f'Processing: {question}')
    try:
        prompt = load_prompt()
        chat_completion = await client.chat.completions.create(
            messages=[*prompt,
                {
                    "role": "user",
                    "content": f'Дай развернутый ответ на вопрос {question}',
                }
            ],
            model="gpt-4o-mini",
        )
    except OpenAIError as e:
        logging.error(f"OpenAI API error for question '{question.title}': {str(e)}")
        return ""
    except Exception as e:
        logging.error(f"Unexpected error processing question '{question.title}': {str(e)}")
        return ""
    return chat_completion.choices[0].message.content
