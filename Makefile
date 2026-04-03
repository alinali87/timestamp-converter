.PHONY: run test install build publish

run:
	uv run python src/timestamp_converter/converter.py

test:
	uv run pytest

install:
	uv sync

build:
	uv build

publish:
	uv publish --index test-pypi
