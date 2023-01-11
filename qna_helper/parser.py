import pandas as pd


def normalize(questions):
    return [question.rstrip() for question in questions]


def parse_questions(path_to_csv):
    df = pd.read_csv(path_to_csv, header=None, delimiter=";")
    return df.iloc[1::2, 4].to_list()


def get_questions(path_to_csv):
    questions = parse_questions(path_to_csv)
    return normalize(questions)
