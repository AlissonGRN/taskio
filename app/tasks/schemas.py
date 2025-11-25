from pydantic import BaseModel, ConfigDict
import uuid
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
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
    completed_at: datetime | None = None
    owner_id: uuid.UUID
    model_config = ConfigDict(from_attributes=True)

