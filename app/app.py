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


@app.post("/tasks/")
async def create_task(session: AsyncSession = Depends(get_async_session), title: str = "New Task", description: str = None):
    new_task = Task(title=title, description=description)
    session.add(new_task)
    await session.commit()
    await session.refresh(new_task)
    return new_task

@app.post("/tasks/complete/{task_id}")
async def complete_task(task_id: str, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()
    if task:
        task.completed = True
        await session.commit()
        await session.refresh(task)
        return task
    return {"error": "Task not found"}

@app.put("/tasks/update/{task_id}")
async def update_task(task_id: str, title: str = None, description: str = None, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()
    if task:
        if title:
            task.title = title
        if description:
            task.description = description
        await session.commit()
        await session.refresh(task)
        return task
    return {"error": "Task not found"}

@app.delete("/tasks/delete/{task_id}")
async def delete_task(task_id: str, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()
    if task:
        await session.delete(task)
        await session.commit()
        return {"message": "Task deleted"}
    return {"error": "Task not found"}

@app.get("/tasks/done")
async def get_completed_tasks(
    session: AsyncSession = Depends(get_async_session)
):
    result = await session.execute(select(Task).where(Task.completed == True).order_by(Task.created_at))
    tasks = result.scalars().all()
    return tasks

@app.get("/tasks/pending")
async def get_pending_tasks(
    session: AsyncSession = Depends(get_async_session)
):
    result = await session.execute(select(Task).where(Task.completed == False).order_by(Task.created_at))
    tasks = result.scalars().all()
    return tasks

