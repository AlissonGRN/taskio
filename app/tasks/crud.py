import datetime
import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from . import models, schemas

async def get_task_by_id(db: AsyncSession, task_id: str) -> models.Task | None:
    result = await db.execute(select(models.Task).where(models.Task.id == task_id))
    return result.scalar_one_or_none()

async def get_tasks(db: AsyncSession, user_id:uuid.UUID, completed: bool | None = None) -> list[models.Task]:
    
    query = select(models.Task).where(models.Task.owner_id == user_id)
    
    if completed is True:
        query = query.where(models.Task.completed == True)
    elif completed is False:
        query = query.where(models.Task.completed == False)
    
    query = query.order_by(models.Task.created_at)
    result = await db.execute(query)
    return result.scalars().all()

async def create_task(db: AsyncSession,user_id:uuid.UUID, task: schemas.TaskCreate) -> models.Task:
    new_task = models.Task(**task.model_dump(), owner_id=user_id)
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task

async def update_task(db: AsyncSession, db_task: models.Task, task_in: schemas.TaskUpdate) -> models.Task:
    update_data = task_in.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(db_task, key, value)
        
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def complete_task(db: AsyncSession, db_task: models.Task) -> models.Task:
    db_task.completed = True
    db_task.completed_at = datetime.utcnow()
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def delete_task(db: AsyncSession, db_task: models.Task) -> None:
    await db.delete(db_task)
    await db.commit()
    return