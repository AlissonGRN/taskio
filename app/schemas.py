from pydantic import BaseModel
import uuid

class TaskCreate(BaseModel):
    title: str
    description: str | None = None

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

class TaskRead(BaseModel):
    id: str
    title: str
    description: str | None = None
    completed: bool
    created_at: str

    class Config:
        orm_mode = True

