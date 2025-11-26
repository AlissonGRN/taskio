import datetime
import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from . import models, schemas

async def get_task_by_id(db: AsyncSession, task_id: str) -> models.Task | None:
    result = await db.execute(select(models.Task).where(models.Task.id == task_id))
    return result.scalar_one_or_none()

async def get_tasks(
    db: AsyncSession, 
    user_id:uuid.UUID,
    page: int,
    size: int,
    completed: bool | None = None
) -> dict:
    
    query = select(models.Task).where(models.Task.owner_id == user_id)
    
    if completed is not None:
        query = query.where(models.Task.completed == completed)

    count_query = select(func.count()).select_from(query.subquery())
    total_result = await db.execute(count_query)
    total = total_result.scalar_one()

    offset = (page - 1)* size
    query = query.order_by(models.Task.created_at.desc())
    query = query.offset(offset).limit(size)

    result = await db.execute(query)
    tasks = result.scalars().all()
    return {
        "items": tasks,
        "total": total,
        "page": page,
        "size": size,
        "pages": (total + size - 1) // size if size > 0 else 0 # arredonda as paginas para cima
    }

    return

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
    db_task.completed_at = datetime.datetime.utcnow()
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def delete_task(db: AsyncSession, db_task: models.Task) -> None:
    await db.delete(db_task)
    await db.commit()
    return