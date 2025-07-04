from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from app.database import Base


class Task(Base):
    """
    SQLAlchemy model for a Task object.
    Represents a to-do item in the tasks table.
    """
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)  # Unique ID for each task
    title = Column(String, nullable=False)              # Title of the task (required)
    description = Column(String, nullable=True)         # Optional description
    is_completed = Column(Boolean, default=False)       # Task completion status
    created_at = Column(                                 
        DateTime(timezone=True),
        server_default=func.now()
    )  # Timestamp of creation, defaults to current time
