FROM python:3.11-slim

RUN apt-get update
RUN apt-get install -y make

RUN pip install poetry requests

ENV PATH /root/.poetry/bin:$PATH

WORKDIR /app

ENV VIRTUAL_ENV /app/.venv
ENV PATH $VIRTUAL_ENV/bin:$PATH
