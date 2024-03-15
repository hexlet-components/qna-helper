from qna_helper.cli import parse_args
from qna_helper.answerer import get_questions
from qna_helper.answerer import get_answers_and_write
import asyncio


def main():
    input_file, output_file = parse_args()
    questions = get_questions(input_file)
    asyncio.run(get_answers_and_write(questions, output_file))


if __name__ == '__main__':
    main()
