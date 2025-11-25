import uuid
from typing import Optional
from datetime import datetime
from fastapi_users import schemas

class UserRead(schemas.BaseUser[uuid.UUID]):
    first_name: Optional[str]
    last_name: Optional[str]
    created_at: datetime

class UserCreate(schemas.BaseUserCreate):
    first_name: Optional[str]
    last_name: Optional[str]

class UserUpdate(schemas.BaseUserUpdate):
    first_name: Optional[str]
    last_name: Optional[str]