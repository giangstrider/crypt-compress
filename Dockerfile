FROM python:3.7-slim

COPY . /
WORKDIR /
RUN apt-get update && apt-get install -y gnupg && pip install pipenv
RUN pipenv install