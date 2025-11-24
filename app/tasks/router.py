from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud, models, schemas
from ..db import get_async_session
from . import models

router = APIRouter(
    prefix="/tasks",  
    tags=["Tasks"]    
)

async def get_task_or_404(
    task_id: str, 
    db: AsyncSession = Depends(get_async_session)
) -> models.Task:
    db_task = await crud.get_task_by_id(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return db_task


@router.post("/", response_model=schemas.TaskRead, status_code=status.HTTP_201_CREATED)
async def create_new_task(
    task: schemas.TaskCreate,
    db: AsyncSession = Depends(get_async_session)
):
    return await crud.create_task(db=db, task=task)


@router.get("/", response_model=list[schemas.TaskRead])
async def read_tasks(
    db: AsyncSession = Depends(get_async_session)
):
    return await crud.get_tasks(db=db)


@router.get("/done", response_model=list[schemas.TaskRead])
async def read_completed_tasks(
    db: AsyncSession = Depends(get_async_session)
):
    return await crud.get_tasks(db=db, completed=True)


@router.get("/pending", response_model=list[schemas.TaskRead])
async def read_pending_tasks(
    db: AsyncSession = Depends(get_async_session)
):
    return await crud.get_tasks(db=db, completed=False)


@router.post("/complete/{task_id}", response_model=schemas.TaskRead)
async def mark_task_complete(
    db_task: models.Task = Depends(get_task_or_404),
    db: AsyncSession = Depends(get_async_session)
):
    return await crud.complete_task(db=db, db_task=db_task)


@router.put("/update/{task_id}", response_model=schemas.TaskRead)
async def update_existing_task(
    task_in: schemas.TaskUpdate, # Usa o schema de update
    db_task: models.Task = Depends(get_task_or_404),
    db: AsyncSession = Depends(get_async_session)
):
    return await crud.update_task(db=db, db_task=db_task, task_in=task_in)


@router.delete("/delete/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_existing_task(
    db_task: models.Task = Depends(get_task_or_404),
    db: AsyncSession = Depends(get_async_session)
):
    await crud.delete_task(db=db, db_task=db_task)
    return None