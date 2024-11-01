import csv
import pytest

from qna_helper.answerer import Question, get_answers_and_write


@pytest.fixture
def question():
    question = Question(
        1,
        'test-slug',
        'test-category',
        'How to create a new project?',
        'https://test-link.com'
    )
    return question


@pytest.mark.vcr()
@pytest.mark.asyncio
async def test_get_answers_and_write(question, tmp_path):
    output_path = tmp_path / 'answers.csv'
    await get_answers_and_write([question], output_path)
    with open(output_path, 'r') as file:
        reader = csv.reader(file)
        assert next(reader) == ['id', 'slug', 'category', 'title', 'link', 'answer']
        # Check that the answer is not empty
        assert next(reader)[3] is not None
