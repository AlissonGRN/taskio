import uuid
from sqlalchemy import Boolean, Column, ForeignKey, String, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from fastapi_users_db_sqlalchemy.generics import GUID
from ..db import Base

class Task(Base):
    __tablename__ = "tasks"

    id: Column = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    title: Column = Column(String, nullable=False)
    description: Column = Column(String, nullable=True)
    completed: Column = Column(Boolean, default=False, nullable=False)
    created_at: Column = Column(DateTime, default=datetime.utcnow)
    completed_at: Column = Column(DateTime, nullable=True)
    owner_id: Column = Column(GUID, ForeignKey("users.id"), nullable=False)
    owner = relationship("User", back_populates="tasks")
    