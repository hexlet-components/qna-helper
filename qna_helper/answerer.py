from dotenv import load_dotenv
from openai import AsyncOpenAI
import csv
import json
import logging
from collections import namedtuple
import asyncio
from contextlib import asynccontextmanager

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
        prompt = json.loads(open('prompt.json').read())
        chat_completion = await client.chat.completions.create(
            messages=[*prompt,
                {
                    "role": "user",
                    "content": f'Дай развернутый ответ на вопрос {question}',
                }
            ],
            model="gpt-3.5-turbo",
        )
        logging.info(chat_completion)
        return chat_completion.choices[0].message.content
    except Exception as e:
        logging.debug(f"Skipped {question}")
        logging.debug(e)
