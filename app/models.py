from re import L
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.sql.operators import is_comparison
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    is_completed = Column(Boolean, default=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
