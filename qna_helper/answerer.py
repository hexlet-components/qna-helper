import os
from openai import OpenAI
import pandas as pd
import logging

from alive_progress import alive_bar

logging.basicConfig(level=logging.INFO)

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_KEY"),
)


def convert(df_of_answers, output_path):
    df_of_answers.to_csv(output_path)


def make_answers(questions, output_path):
    result = pd.DataFrame()
    with alive_bar(len(questions)) as move_bar:
        for question in questions:
            answer = get_answer(question)
            answer_df = pd.Series({question: answer})
            result = pd.concat([result, answer_df])
            move_bar()
    convert(result, output_path)


def get_answer(question):
    logging.info(f'Processing: {question}')
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f'развернутый ответ на вопрос {question}',
                }
            ],
            model="gpt-3.5-turbo",
        )
        print(chat_completion)
        return chat_completion.choices[0].message.content
    except Exception:
        logging.info(f"Skipped {question}")
