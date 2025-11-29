from sqlalchemy.ext.asyncio import create_async_engine
from src.config import CONFIG
from sqlalchemy import text
from src.db.models import Base, User

DB_URL = f"postgresql+asyncpg://{CONFIG.POSTGRES_USER}:{CONFIG.POSTGRES_PASSWORD}@db/{CONFIG.POSTGRES_DB}"

engine = create_async_engine(
    url=DB_URL,
    echo=True
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("Database initialized and tables created if they did not exist.")
