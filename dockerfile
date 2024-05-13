# FROM python:3.10-slim as jupyter-local
FROM bitnami/spark:3.5.1 as jupyter-local

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

WORKDIR /app

EXPOSE 8888
