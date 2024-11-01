FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y make && \
    pip install uv

RUN adduser --disabled-password --gecos '' myuser

ENV UV_LINK_MODE=copy
ENV UV_COMPILE_BYTECODE=1
RUN --mount=type=cache,target=/root/.cache/uv

WORKDIR /app
COPY . .

RUN chown -R myuser:myuser /app

USER myuser
