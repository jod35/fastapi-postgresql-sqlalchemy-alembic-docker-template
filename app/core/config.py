from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    DATABASE_URL: str = "postgresql://postgres:postgres@db:5432/app_db"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
