FROM python:3.8-slim
MAINTAINER Chins Kuriakose, chinskuriakose01@gmail.com

COPY sample_files sample_files
COPY src src
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
WORKDIR src

ENTRYPOINT python main.py
