import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_get_tasks_unauthorized(client: AsyncClient):
    response = await client.get("/tasks/")
    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized"}

@pytest.mark.asyncio
async def test_create_task_and_list_task_flow(client: AsyncClient, session):

    user_data = {
  "email": "user@example.com",
  "password": "password123",
  "is_active": True,
  "is_superuser": False,
  "is_verified": False,
  "first_name": "user",
  "last_name": "name"
}

    # Register a new user
    response = await client.post("/auth/register", json=user_data)
    assert response.status_code == 201

    # Log in to get the access token
    login_data = {
        "username": user_data["email"],
        "password": user_data["password"]
    }
    response_login = await client.post("/auth/jwt/login", data=login_data)

    # Extract the access token
    token = response_login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Create a new task
    task_data = {"title": "Test Task", "description": "This is a test task."}
    response_create = await client.post("/tasks/", json=task_data, headers=headers)
    assert response_create.status_code == 201
    data = response_create.json()
    assert data["title"] == task_data["title"]
    assert "id" in data

    # List tasks to verify the created task is present
    response_list = await client.get("/tasks/", params={"page": 1, "size": 10, "completed": False}, headers=headers)
    assert response_list.status_code == 200
    items = response_list.json()["items"]
    assert len(items) == 1
    assert items[0]["title"] == task_data["title"]