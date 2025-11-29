from fastapi import FastAPI

from app.api.users import router as users_router

app = FastAPI(
    title="FastAPI PostgreSQL Template",
    description="A template for FastAPI with PostgreSQL, SQLAlchemy, Alembic, and Docker",
    version="1.0.0",
)


@app.get("/")
def root():
    """Root endpoint."""
    return {"message": "Welcome to FastAPI PostgreSQL Template"}


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


# Include routers
app.include_router(users_router, prefix="/api/v1")
