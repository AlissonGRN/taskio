import uuid
from collections.abc import AsyncGenerator
from sqlalchemy import Boolean, Column, String, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from fastapi import Depends
from datetime import datetime



DATABASE_URL = "sqlite+aiosqlite:///./tasks.db"

class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__ = "tasks"

    id: Column = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    title: Column = Column(String, nullable=False)
    description: Column = Column(String, nullable=True)
    completed: Column = Column(Boolean, default=False, nullable=False)
    created_at: Column = Column(DateTime, default=datetime.utcnow)

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

