from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=True, 
    autoflush=True, 
    bind=engine
)

Base = declarative_base()