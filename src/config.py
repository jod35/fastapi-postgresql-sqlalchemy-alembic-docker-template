from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra ="ignore"
    )

CONFIG = Settings()