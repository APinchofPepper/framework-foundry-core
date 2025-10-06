# Framework Foundry Core

Core backend for Framework Foundry — a system for building reusable web-app frameworks for small businesses.

## Tech Stack
- **Backend:** FastAPI  
- **Database:** PostgreSQL  
- **Deployment:** Docker + GitHub Actions  
- **Language:** Python 3.11

## Setup
1. Clone the repo  
2. Create `.env` based on `.env.example`  
3. Run with Docker (coming Day 2)

## Developer Commands

| Command | Description |
|----------|--------------|
| `make up` | Build and start backend + db |
| `make down` | Stop containers and remove volumes |
| `make test` | Run test suite |
| `make fmt` | Auto-format code |
| `make lint` | Run flake8 checks |

