from dotenv import load_dotenv

from qna_helper.cli import parse_args
from qna_helper.parser import get_questions
from qna_helper.answerer import make_answers

load_dotenv()


def main():
    input_file, output_file = parse_args()
    questions = get_questions(input_file)
    make_answers(questions, output_file)


if __name__ == '__main__':
    main()
