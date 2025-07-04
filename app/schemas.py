from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class BaseTaskClass(BaseModel):
    """
    Base schema for shared task attributes.
    Used for both creation and update operations.
    """
    title: str
    description: Optional[str] = None
    is_completed: Optional[bool] = False


class TaskCreate(BaseTaskClass):
    """
    Schema for creating a new task.
    Inherits required fields from BaseTaskClass.
    """
    pass


class TaskUpdate(BaseTaskClass):
    """
    Schema for updating an existing task.
    All fields are optional to allow partial updates.
    """
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None


class TaskInDB(BaseTaskClass):
    """
    Schema for reading a task from the database.
    Includes read-only fields like ID and timestamp.
    """
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)  # Allow conversion from ORM objects
