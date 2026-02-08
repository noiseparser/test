.PHONY: help install dev lint test clean

help:
	@echo "Targets:"
	@echo "  install  install the package"
	@echo "  dev      install in editable mode with dev extras"
	@echo "  lint     run flake8 over the source tree"
	@echo "  test     run the test suite"
	@echo "  clean    remove build and cache artifacts"

install:
	python3 -m pip install .

dev:
	python3 -m pip install -e ".[dev]"

lint:
	python3 -m flake8 src tests

test:
	python3 -m pytest

clean:
	rm -rf build dist *.egg-info src/*.egg-info
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
