install:
	poetry install

qna-helper:
	poetry run qna-helper

build:
	poetry build

package-install:
	python -m pip install --user dist/*.whl

lint:
	poetry run flake8 qna_helper

fast-install: build package-install
