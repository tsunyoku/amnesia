# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR /amnesia

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN apt-get -y update
RUN apt-get install -y postgresql-client

RUN curl -L https://packagecloud.io/golang-migrate/migrate/gpgkey | apt-key add -
RUN echo "deb https://packagecloud.io/golang-migrate/migrate/debian bullseye main" > /etc/apt/sources.list.d/migrate.list
RUN apt-get -y update
RUN apt-get -y install migrate

CMD scripts/start.sh
