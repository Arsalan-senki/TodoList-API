import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Define log directory and file
log_dir = Path(__file__).resolve().parent / "logs"
log_dir.mkdir(parents=True, exist_ok=True)
log_file = log_dir / "error.log"

# Configure rotating file handler
file_handler = RotatingFileHandler(
    log_file,
    maxBytes=1_000_000,
    backupCount=3
)
file_handler.setFormatter(logging.Formatter(
    "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
))

# Create logger instance
logger = logging.getLogger("app_logger")
logger.setLevel(logging.ERROR)
logger.addHandler(file_handler)
logger.propagate = False  # Prevent duplicate logs if root logger is configured elsewhere
