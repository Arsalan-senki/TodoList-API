from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL

# Create engine
engine = create_engine(DATABASE_URL)

# Create a session factory (no autocommit/autoflush)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

# Base class for models
Base = declarative_base()
