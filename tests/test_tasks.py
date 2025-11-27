import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_get_tasks_unauthorized(client: AsyncClient):
    response = await client.get("/tasks/")
    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized"}