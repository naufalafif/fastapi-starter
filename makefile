run:
	uvicorn app.main:app --reload

build:
	docker build -t fastapi-starer .