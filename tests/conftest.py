import pytest
from typing import AsyncGenerator
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.pool import StaticPool

from app.db import Base, get_async_session
from app.app import app

DATABASE_URL_TEST = "sqlite+aiosqlite:///:memory:"

engine_test = create_async_engine(
    DATABASE_URL_TEST,
    poolclass=StaticPool,
)

async_session_maker_test = async_sessionmaker(
    engine_test,
    expire_on_commit=False,
)

@pytest.fixture
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture
async def session(prepare_database) -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker_test() as session:
        yield session

@pytest.fixture
async def client(session) -> AsyncGenerator[AsyncClient, None]:
    
    app.dependency_overrides[get_async_session] = lambda: session

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac

    app.dependency_overrides.clear()


