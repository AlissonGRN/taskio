from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from app.db import create_db_and_tables, get_async_session, Task


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/tasks/")
async def get_tasks(
    session: AsyncSession = Depends(get_async_session)
):
    result = await session.execute(select(Task).order_by(Task.created_at))
    tasks = result.scalars().all()
    return tasks


