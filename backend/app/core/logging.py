import logging
import os
from logging.handlers import RotatingFileHandler

# Create logger
logger = logging.getLogger("framework_foundry")
logger.setLevel(logging.INFO)

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# File handler with rotation
handler = RotatingFileHandler("logs/app.log", maxBytes=5 * 1024 * 1024, backupCount=3)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def log_info(message: str):
    logger.info(message)


def log_error(message: str):
    logger.error(message)


def log_warning(message: str):
    logger.warning(message)
