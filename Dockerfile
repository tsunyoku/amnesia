# syntax=docker/dockerfile:1

FROM python:3.10

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /amnesia
CMD ["make", "run-bare"]
