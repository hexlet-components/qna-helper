compose-setup: compose-build compose-app-setup

compose-build:
	docker compose build

compose-app-setup:
	docker compose run app make setup

compose-bash:
	docker compose run --rm app bash

compose:
	docker compose up --abort-on-container-exit

setup:
	uv sync
	cp -n .env.example .env

qna-helper:
	uv run qna-helper

lint:
	uv run ruff check qna_helper
