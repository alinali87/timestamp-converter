.PHONY: run test install build publish

run:
	poetry run python src/timestamp_converter/converter.py

test:
	poetry run pytest

install:
	poetry install

build:
	poetry build

publish:
	poetry publish -r test-pypi
