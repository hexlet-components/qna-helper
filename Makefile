compose-setup: compose-build compose-app-setup

compose-build:
	docker compose build

compose-app-setup:
	docker compose run app make setup

compose-bash:
	docker compose run --rm app bash

compose:
	docker compose up

setup:
	poetry install
	cp -n .env.example .env

qna-helper:
	poetry run qna-helper

lint:
	poetry run flake8 qna_helper
