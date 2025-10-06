from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from app.core.config import settings
import time
import logging

logger = logging.getLogger(__name__)

def create_engine_with_retry(database_url: str, max_retries: int = 30, retry_delay: float = 1.0):
    """Create database engine with retry logic for connection issues."""
    for attempt in range(max_retries):
        try:
            engine = create_engine(database_url)
            # Test the connection
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            logger.info("Database connection established successfully")
            return engine
        except OperationalError as e:
            if attempt < max_retries - 1:
                logger.warning(f"Database connection attempt {attempt + 1} failed: {e}. Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
                retry_delay = min(retry_delay * 1.5, 10.0)  # Exponential backoff, max 10 seconds
            else:
                logger.error(f"Failed to connect to database after {max_retries} attempts")
                raise

engine = create_engine_with_retry(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
