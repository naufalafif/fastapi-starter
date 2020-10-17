run:
	uvicorn app.main:app --reload

build:
	docker build -t fastapi-starer .

doctest:
	poetry run xdoctest -m app

static-type-check:
	poetry run mypy app/main.py