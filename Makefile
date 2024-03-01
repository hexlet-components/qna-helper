env-prepare:
	cp -n .env.example .env

install: env-prepare
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

compose-build:
	docker compose build

compose-bash:
	docker compose run --rm app bash

run:
	poetry run qna-helper -i questions.csv
