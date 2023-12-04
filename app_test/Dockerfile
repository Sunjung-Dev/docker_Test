FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-2020-04-12
LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

WORKDIR .
COPY ./ ./
RUN pip install --no-cache-dir -r requirements.txt
