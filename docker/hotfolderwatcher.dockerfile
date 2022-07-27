FROM python:3.10.5-alpine

ARG DEBIAN_FRONTEND=noninteractive

RUN mkdir app/
WORKDIR app/

EXPOSE 8081

RUN apk update
RUN pip install --upgrade pip

RUN apk add git
RUN apk add db-dev
RUN apk add db
RUN apk add gcc
RUN apk add musl-dev

RUN pip install berkeleydb
RUN pip install rdflib
RUN pip install watchdog

RUN git clone https://github.com/theophpo/semantic-indexer.git

ENTRYPOINT python semantic-indexer/API/hotfolderWatcher.py
