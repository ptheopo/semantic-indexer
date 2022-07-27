FROM python:3.10.5-alpine

ARG DEBIAN_FRONTEND=noninteractive

RUN mkdir app/
WORKDIR app/

EXPOSE 5000

RUN apk update
RUN pip install --upgrade pip

RUN apk add gcc
RUN apk add git
RUN apk add db
RUN apk add db-dev
RUN apk add musl-dev

RUN pip install rdflib
RUN pip install flask
RUN pip install flask-cors
RUN pip install berkeleydb

RUN git clone https://github.com/theophpo/semantic-indexer.git

CMD cd semantic-indexer/API && python domain.py
