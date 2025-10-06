from contextlib import asynccontextmanager

from app.api.routes import auth
from app.core.database import Base, engine
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown (if needed)


app = FastAPI(title="Framework Foundry Core API", lifespan=lifespan)

app.include_router(auth.router, prefix="/auth", tags=["auth"])


@app.get("/")
def root():
    return {"message": "Framework Foundry Core API running"}
