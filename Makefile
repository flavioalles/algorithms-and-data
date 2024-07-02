.PHONY: install
install:
	@poetry install --with=dev

.PHONY: tests
test:
	@poetry run pytest --verbose tests