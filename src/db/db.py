from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import select

from src.core.configs import Settings


'''
Подключение к серверу
'''
DB_URL = Settings.DB_URL
engine = create_async_engine(DB_URL)
'''
Создание сессии для работы с БД
'''
async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
"""
Создание моделей для БД
"""
class Base(DeclarativeBase):
    pass
"""
функции создания  и удаления БД
"""
async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)



