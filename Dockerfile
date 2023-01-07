FROM python:3.10

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install -U pip setuptools
RUN pip install -r requirements.txt

RUN apt update && \
    apt install -y default-mysql-client

RUN wget https://github.com/golang-migrate/migrate/releases/download/v4.15.2/migrate.linux-amd64.tar.gz && \
    tar zxvf migrate.linux-amd64.tar.gz && \
    mv migrate /usr/local/bin/go-migrate && \
    chmod u+x /usr/local/bin/go-migrate && \
    rm migrate.linux-amd64.tar.gz

COPY scripts /scripts
COPY ext /ext
RUN chmod u+x /scripts/*

COPY mount /srv/root
WORKDIR /srv/root

EXPOSE 80
