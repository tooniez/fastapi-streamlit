.PHONY: install run-api run-streamlit format test docker-build-api docker-build-streamlit

install:
	pip3 install -r api/requirements.txt
	pip3 install -r app/requirements.txt
	pip3 install -r requirements-dev.txt

run-api:
	fastapi dev api/server.py

run-streamlit:
	streamlit run app/streamlit_app.py

format:
	black .

test:
	pytest

docker-build:
	docker build -t fastapi-base:latest -f api/Dockerfile .
	docker build -t streamlit-base:latest -f app/Dockerfile .

all: install format docker-build test
