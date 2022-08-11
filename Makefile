#!/usr/bin/make

mypy:
	@mypy . --explicit-package-bases --namespace-packages --exclude venv

run-bare:
	@./main.py

build:
	@docker build -t amnesia:latest .

run:
	@docker-compose up --build postgres redis amnesia
