# TaskIO

🇧🇷 [Português](README.md) | [🇬🇧 English](README.en.md)

Asynchronous RESTful API for task management with JWT authentication and access control.

## 📋 Description

TaskIO is a backend application developed with **FastAPI** that provides complete task management, user authentication with JWT, pagination, and automated tests. The project demonstrates modern development best practices in Python.

**Access:** [Swagger UI](http://localhost:8000/docs) • [ReDoc](http://localhost:8000/redoc)

---

## ✨ Project Highlights

- ✅ **JWT Authentication**: Secure system with Argon2 password hashing
- ✅ **Access Control**: Each user manages only their own tasks
- ✅ **Pagination**: Listing with page/size and complete metadata
- ✅ **Automated Tests**: Suite with pytest and pytest-asyncio
- ✅ **Async Database**: SQLAlchemy async ready for production
- ✅ **Secure Configuration**: Environment variables with Pydantic Settings
 - ✅ **Database Migrations**: Alembic for schema versioning

---

## 🚀 Features

### Task Management
- Create, list, update, and delete tasks
- Filter by status (pending/completed)
- Pagination with page/size
- Creation and completion timestamps
- Per-user access control

### Authentication and Users
- Registration with email validation
- JWT login (1 hour expiration)
- View and update profile
- Argon2-CFI password hashing

---

## 🛠️ Technologies

- **FastAPI** - High-performance web framework
- **Pydantic v2** - Validation and configuration
- **SQLAlchemy (Async)** - Asynchronous ORM
- **Aiosqlite** - Asynchronous SQLite driver
- **FastAPI-Users** - Authentication and user management
- **Argon2-CFI** - Password hashing
- **pytest** - Automated testing
- **Uvicorn** - ASGI server
 - **Alembic** - Database migration management

---

## 📂 Project Structure

The project follows a layered architecture with clear separation of responsibilities:

- **app/**: Main application with task and authentication modules
- **tests/**: Automated test suite with pytest
- **main.py**: Application entry point
- **.env-exemple**: Configuration template
- **requirements.txt**: Project dependencies

---

## 🔧 Installation and Setup

### Prerequisites
- Python 3.11+
- pip

### Steps

1. Clone the repository:
```bash
git clone https://github.com/AlissonGRN/taskio.git
cd taskio
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env-exemple .env
# Edit .env with SECRET_KEY and DATABASE_URL
```

5. Run database migrations (Alembic):
```bash
# Apply schema migrations to the database
alembic upgrade head

# (optional) Create a new migration after changing models:
alembic revision --autogenerate -m "describe changes"
```

6. Run the application:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

---

## 📚 Endpoints

### Authentication (Public)
- `POST /auth/register` - Register new user
- `POST /auth/jwt/login` - Login (returns JWT)
- `POST /auth/jwt/logout` - Logout

### Tasks (Requires authentication)
- `POST /tasks/` - Create task
- `GET /tasks/` - List with pagination
- `GET /tasks/pending` - List pending tasks
- `GET /tasks/done` - List completed tasks
- `PUT /tasks/update/{id}` - Update task
- `POST /tasks/complete/{id}` - Mark as completed
- `DELETE /tasks/delete/{id}` - Delete task

### User (Requires authentication)
- `GET /users/me` - Get user data
- `PATCH /users/{id}` - Update user

---

## 🧪 Tests

```bash
# Run all tests
pytest

# With verbose output
pytest -v

# With coverage
pytest --cov=app tests/
```

Tests use in-memory database for isolation.

---

## 📊 Roadmap

- ✅ JWT Authentication
- ✅ Task CRUD with access control
- ✅ Pagination
- ✅ Automated tests
- ✅ Configuration with .env
- 📋 PostgreSQL migration
- 🐳 Docker + docker-compose
- 🔄 Refresh tokens
- 📧 Email notifications
- 🏷️ Tags/Categories
- 🚦 Rate limiting

---

Made with ❤️ by Alisson Nascimento
