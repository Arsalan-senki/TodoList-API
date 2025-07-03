from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class BaseTaskClass(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: Optional[bool] = False


class TaskCreate(BaseTaskClass):
    pass


class TaskUpdate(BaseTaskClass):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None


class TaskInDB(BaseTaskClass):
    id: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)