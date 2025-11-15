from pydantic import BaseModel, ConfigDict
import uuid
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(BaseModel):
    pass

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

class TaskRead(BaseModel):
    id: str
    title: str
    description: str | None = None
    completed: bool
    created_at: datetime

    class Config:
        orm_mode = ConfigDict(from_attributes=True)

