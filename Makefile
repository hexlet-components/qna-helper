compose-setup: compose-build compose-app-setup

compose-build:
	docker compose build --no-cache

compose-app-setup:
	docker compose run --rm app make setup

compose-bash:
	docker compose run --rm app bash

compose:
	docker compose up --remove-orphans --abort-on-container-exit

compose-clean:
	docker compose down --volumes --remove-orphans

setup:
	uv sync
	cp -n .env.example .env

qna-helper:
	uv run qna-helper

lint:
	uv run ruff check qna_helper

test:
	uv run pytest -vv -s

check: test lint
