#!/usr/bin/make

mypy:
	@mypy . --explicit-package-bases --namespace-packages --exclude venv

run:
	@./main.py
