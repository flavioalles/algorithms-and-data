.PHONY: install
install:
	@poetry install --with=dev

.PHONY: format
format:
	@poetry run black --target-version py312 src tests

.PHONY: tests
test:
	@poetry run pytest --verbose tests