install:
	poetry install

qna-helper:
	poetry run qna-helper

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 qna_helper

