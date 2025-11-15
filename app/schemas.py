from pydantic import BaseModel, ConfigDict
import uuid
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    """Schema usado na criação — herda de TaskBase para garantir `title` obrigatório."""


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
    model_config = ConfigDict(from_attributes=True)

