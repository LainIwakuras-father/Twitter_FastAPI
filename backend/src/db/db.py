'''
Подключение к серверу
'''
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase



DB_URL = f'postgresql+asyncpg://'

engine = create_async_engine(DB_URL, echo=True)
"""
Создание моделей для БД
"""
class Base(DeclarativeBase):
    pass

"""функции создания и удаления БД
"""
async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


"""
Создание сессии для работы с БД
"""
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
