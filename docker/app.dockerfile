FROM alpine:3.15.5

ARG DEBIAN_FRONTEND=noninteractive

RUN mkdir app/
WORKDIR app/

EXPOSE 8001

RUN apk update
RUN apk add nodejs
RUN apk add npm
RUN apk add git

RUN git clone https://github.com/theophpo/semantic-indexer.git

RUN cd semantic-indexer/APP && npm install

CMD cd semantic-indexer/APP && node app.js
