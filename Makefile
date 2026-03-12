.PHONY: install test lint run

install:
	pip install -e .[dev]

test:
	pytest

lint:
	ruff check src tests scripts

run:
	audio-prep run --input-audio data/input/song.wav --output-json data/output/analysis.json
