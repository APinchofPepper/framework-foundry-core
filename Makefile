.PHONY: help up up-fresh down down-clean build logs shell test fmt lint clean migrate migrate-create migrate-status migrate-reset db-shell db-reset

help:
	@echo "Framework Foundry Core - Available Commands:"
	@echo ""
	@echo "🚀 Development:"
	@echo "  make up          - Start all services"
	@echo "  make up-fresh    - Start fresh environment with clean database"
	@echo "  make down        - Stop all services"
	@echo "  make down-clean  - Stop services and remove volumes"
	@echo "  make build       - Build Docker images"
	@echo "  make logs        - View backend logs"
	@echo "  make shell       - Open backend shell"
	@echo ""
	@echo "🗄️  Database:"
	@echo "  make migrate           - Run database migrations"
	@echo "  make migrate-create    - Create new migration"
	@echo "  make migrate-status    - Check migration status"
	@echo "  make migrate-reset     - Reset database (⚠️  destroys data)"
	@echo "  make db-shell          - Open database shell"
	@echo "  make db-reset          - Drop and recreate database"
	@echo ""
	@echo "🧪 Testing & Quality:"
	@echo "  make test        - Run tests"
	@echo "  make fmt         - Format code"
	@echo "  make lint        - Lint code"
	@echo "  make clean       - Clean Docker system"
	@echo ""
	@echo "📋 Quick Start:"
	@echo "  make down && make up && make migrate"

up:
	docker compose up --build

up-fresh:
	@echo "Starting fresh environment with database setup..."
	docker compose down -v
	docker compose up --build -d
	@echo "Waiting for database to be ready..."
	sleep 10
	docker compose exec backend alembic upgrade head
	@echo "Environment is ready!"

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

# Database migration targets
migrate:
	@echo "Running database migrations..."
	docker compose exec backend alembic upgrade head

migrate-create:
	@echo "Creating new migration..."
	@read -p "Enter migration message: " msg; \
	docker compose exec backend alembic revision --autogenerate -m "$$msg"

migrate-status:
	@echo "Checking migration status..."
	docker compose exec backend alembic current
	@echo "Migration history:"
	docker compose exec backend alembic history --verbose

migrate-reset:
	@echo "⚠️  WARNING: This will reset the database and lose all data!"
	@read -p "Are you sure? (y/N): " confirm; \
	if [ "$$confirm" = "y" ] || [ "$$confirm" = "Y" ]; then \
		docker compose down -v; \
		docker compose up -d db; \
		sleep 5; \
		docker compose exec backend alembic upgrade head; \
		echo "Database reset complete!"; \
	else \
		echo "Reset cancelled."; \
	fi

# Database management targets
db-shell:
	docker compose exec db psql -U postgres -d frameworkfoundry

db-reset:
	@echo "⚠️  WARNING: This will drop and recreate the database!"
	@read -p "Are you sure? (y/N): " confirm; \
	if [ "$$confirm" = "y" ] || [ "$$confirm" = "Y" ]; then \
		docker compose exec db psql -U postgres -c "DROP DATABASE IF EXISTS frameworkfoundry;"; \
		docker compose exec db psql -U postgres -c "CREATE DATABASE frameworkfoundry;"; \
		docker compose exec backend alembic upgrade head; \
		echo "Database recreated successfully!"; \
	else \
		echo "Database reset cancelled."; \
	fi
