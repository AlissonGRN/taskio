from fastapi import FastAPI
from contextlib import asynccontextmanager
from .db import create_db_and_tables
from .routers import tasks 

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(tasks.router)
