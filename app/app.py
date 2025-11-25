from fastapi import FastAPI
from contextlib import asynccontextmanager
from .db import create_db_and_tables
from .tasks import router as task_routers
from .users import router as user_routers 

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(task_routers.router)
app.include_router(user_routers.router)
