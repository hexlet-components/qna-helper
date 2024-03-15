FROM python:3.11-slim

RUN apt-get update
RUN apt-get install -y make

RUN adduser --disabled-password --gecos '' myuser

RUN pip install poetry
ENV PATH /root/.poetry/bin:$PATH
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

WORKDIR /app
COPY . .

RUN chown -R myuser:myuser /app

USER myuser
