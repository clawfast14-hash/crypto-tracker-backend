import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Строка подключения для локальной базы данных SQLite
DATABASE_URL = "sqlite+aiosqlite:///./cryptowatch.db"

engine = create_async_engine(
    DATABASE_URL, 
    echo=True, 
    connect_args={"check_same_thread": False}
)

AsyncSessionLocal = sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session