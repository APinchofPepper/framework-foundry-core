from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/frameworkfoundry")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "changeme")

settings = Settings()
