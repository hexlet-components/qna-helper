import os
import openai
import pandas as pd
import logging

from alive_progress import alive_bar

logging.basicConfig(level=logging.INFO)

openai.api_key = os.getenv("OPENAI_API_KEY")


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
        answer = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{question}",
            max_tokens=1300,
            temperature=0.45,
            best_of=1
        )
        return answer.choices[0].text
    except Exception:
        logging.info(f"Skipped {question}")
