# FROM python:3.10-slim as jupyter-local
FROM bitnami/spark:3.5.1 as jupyter-local

WORKDIR /app

COPY requirements/requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8888
