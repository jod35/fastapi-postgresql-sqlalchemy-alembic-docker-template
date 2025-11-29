# FastAPI PostgreSQL SQLAlchemy Alembic Docker Template

A template to build a FastAPI project with FastAPI, PostgreSQL, SQLAlchemy, and Alembic inside Docker.

## Features

- **FastAPI** - Modern, fast web framework for building APIs
- **PostgreSQL** - Powerful, open-source relational database
- **SQLAlchemy** - SQL toolkit and ORM for Python
- **Alembic** - Database migration tool for SQLAlchemy
- **Docker & Docker Compose** - Containerization for consistent development environments

## Project Structure

```
.
├── alembic/                 # Alembic migrations
│   ├── versions/            # Migration files
│   ├── env.py               # Alembic environment configuration
│   └── script.py.mako       # Migration script template
├── app/
│   ├── api/                 # API endpoints
│   │   └── users.py         # User endpoints
│   ├── core/                # Core configuration
│   │   └── config.py        # Application settings
│   ├── db/                  # Database configuration
│   │   └── session.py       # SQLAlchemy session setup
│   ├── models/              # SQLAlchemy models
│   │   └── user.py          # User model
│   ├── schemas/             # Pydantic schemas
│   │   └── user.py          # User schemas
│   └── main.py              # FastAPI application entry point
├── alembic.ini              # Alembic configuration
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile               # Docker image configuration
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup

1. Clone the repository:

```bash
git clone https://github.com/jod35/fastapi-postgresql-sqlalchemy-alembic-docker-template.git
cd fastapi-postgresql-sqlalchemy-alembic-docker-template
```

2. Copy the environment file:

```bash
cp .env.example .env
```

3. Build and start the containers:

```bash
docker-compose up --build
```

4. The API will be available at `http://localhost:8000`

### Running Migrations

Create a new migration:

```bash
docker-compose exec web alembic revision --autogenerate -m "Your migration message"
```

Apply migrations:

```bash
docker-compose exec web alembic upgrade head
```

Rollback migration:

```bash
docker-compose exec web alembic downgrade -1
```

## API Endpoints

### Health Check
- `GET /` - Welcome message
- `GET /health` - Health check endpoint

### Users
- `POST /api/v1/users/` - Create a new user
- `GET /api/v1/users/` - Get all users
- `GET /api/v1/users/{user_id}` - Get a user by ID
- `DELETE /api/v1/users/{user_id}` - Delete a user

## API Documentation

Once the application is running, you can access:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Development

To run the application in development mode with hot-reload:

```bash
docker-compose up
```

To stop the containers:

```bash
docker-compose down
```

To stop and remove volumes:

```bash
docker-compose down -v
```

## License

MIT
