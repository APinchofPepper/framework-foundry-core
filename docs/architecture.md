# Framework Foundry Core Architecture

This document describes the technical structure and conventions for the Framework Foundry core platform.

## Overview

Framework Foundry Core provides the foundation for all modular frameworks (TherapyPortal, LocalCMS, etc.). It includes:

- **FastAPI backend** for APIs
- **PostgreSQL database** for persistence
- **Docker Compose** for environment management
- **GitHub Actions** for CI/CD
- **SQLAlchemy ORM** for models and migrations

## Folder Layout

```
backend/
├── app/
│   ├── core/          # Config, DB setup, utils
│   ├── models/        # SQLAlchemy models
│   ├── routes/        # API endpoints
│   └── tests/         # pytest test suite
```

## Development Commands

```bash
# Start all services
docker compose up --build

# Run tests
docker compose exec backend pytest app/tests -v

# Stop and remove volumes
docker compose down -v
```

## Future Modules

- Auth system (JWT)
- Dashboard routes
- Client management APIs
- Admin panel

## Setup Instructions

### 1. Create `.env.example`

```bash
DATABASE_URL=postgresql://postgres:postgres@db:5432/frameworkfoundry
SECRET_KEY=changeme
DEBUG=True
```

### 2. Update README.md

Add a quickstart section:

```markdown
## Quickstart

1. Clone the repo
2. Copy `.env.example` → `.env`
3. Build and run:
   ```bash
   docker compose up --build
   ```
4. Visit http://localhost:8000

### Run tests:

```bash
docker compose exec backend pytest app/tests -v
```

### 3. Commit Changes

```bash
git add .
git commit -m "Add documentation and .env.example for local setup"
git push
```