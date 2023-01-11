import argparse
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        prog='qna-helper',
        usage='qna-helper [options]',
        description='answer questions using davinci-003',
        add_help=False,
    )
    parser.add_argument(
        '-h',
        '--help',
        action='help',
        help='dispaly help for command',
    )
    parser.add_argument(
        '-i',
        '--input_file',
        default=Path('questions.csv'),
        help='csv file to parse',
        type=str,
    )
    parser.add_argument(
        '-o',
        '--output_file',
        default=Path('new_answers.csv'),
        help='csv file to save answers',
        type=str,
    )
    args = parser.parse_args()
    return args.input_file, args.output_file
