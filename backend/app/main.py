from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.database import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown (if needed)


app = FastAPI(title="Framework Foundry Core API", lifespan=lifespan)


@app.get("/")
def root():
    return {"message": "Framework Foundry Core API running"}
