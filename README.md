# Framework Foundry Core

Core backend for Framework Foundry — a system for building reusable web-app frameworks for small businesses.

## Tech Stack
- **Backend:** FastAPI  
- **Database:** PostgreSQL  
- **Deployment:** Docker + GitHub Actions  
- **Language:** Python 3.11
- **Frontend:** React + Vite

## Quick Start

```bash
# Clone and setup
git clone <repo-url>
cd framework-foundry-core

# Start everything with fresh database
make up-fresh

# Or step by step:
make up && make migrate
```

## Available Commands

Run `make help` to see all available commands.

### 🚀 Development Commands

| Command | Description |
|---------|-------------|
| `make up` | Start all services |
| `make up-fresh` | Start fresh environment with clean database |
| `make down` | Stop all services |
| `make down-clean` | Stop services and remove volumes |
| `make build` | Build Docker images |
| `make logs` | View backend logs |
| `make shell` | Open backend shell |

### 🗄️ Database Management

| Command | Description |
|---------|-------------|
| `make migrate` | Run database migrations |
| `make migrate-create` | Create new migration (interactive) |
| `make migrate-status` | Check migration status and history |
| `make migrate-reset` | Reset database (⚠️ destroys data) |
| `make db-shell` | Open PostgreSQL shell |
| `make db-reset` | Drop and recreate database |

### 🧪 Testing & Quality

| Command | Description |
|---------|-------------|
| `make test` | Run test suite |
| `make fmt` | Auto-format code |
| `make lint` | Run flake8 checks |
| `make clean` | Clean Docker system |

## Common Workflows

### Daily Development
```bash
make up && make migrate
```

### Fresh Start (Clean Database)
```bash
make up-fresh
```

### Adding Database Changes
```bash
# After modifying models
make migrate-create
# Enter migration message when prompted
make migrate
```

### Troubleshooting Database Issues
```bash
make migrate-status  # Check current state
make db-shell        # Direct database access
```

## Features

### ✅ Implemented
- **User Authentication:** JWT-based auth with registration/login
- **User Management:** Role-based access (user/admin)
- **Notifications:** Real-time notification system
- **Admin Dashboard:** User statistics and management
- **Database Migrations:** Alembic with proper versioning
- **API Documentation:** Auto-generated OpenAPI docs

### 🔄 In Development
- Client management system
- Framework templates
- Email notifications
- File upload handling

## API Endpoints

- **Auth:** `/auth/register`, `/auth/login`
- **Users:** `/users/me`
- **Admin:** `/admin/stats`
- **Notifications:** `/notifications/`, `/notifications/{id}/read`

## Environment Setup

Create `.env` file:
```bash
DATABASE_URL=postgresql://postgres:postgres@db:5432/frameworkfoundry
SECRET_KEY=your-secret-key-here
DEBUG=True
```

## Development Notes

- Database migrations are managed with Alembic
- All database operations go through SQLAlchemy ORM
- Frontend runs on port 5173, backend on port 8000
- PostgreSQL runs on port 5433 (mapped from container port 5432)

