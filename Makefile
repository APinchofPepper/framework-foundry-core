.PHONY: up down down-clean build logs shell test fmt lint clean migrate

up:
	docker compose up --build

down:
	docker compose down

down-clean:
	docker compose down -v

build:
	docker compose build

logs:
	docker compose logs -f backend

shell:
	docker compose exec backend bash

test:
	docker compose exec backend pytest app/tests -v

fmt:
	docker compose exec backend black app
	docker compose exec backend isort app

lint:
	docker compose exec backend flake8 app

clean:
	docker system prune -f

migrate:
	docker compose exec backend alembic upgrade head
