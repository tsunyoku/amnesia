#!/usr/bin/make

mypy:
	@mypy . --explicit-package-bases --namespace-packages --exclude venv

run-bare:
	@./main.py

build:
	@docker build .

run:
	@docker-compose up mysql redis amnesia
