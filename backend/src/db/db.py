from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from backend.src.db.configs import DB_USER, DB_PASS, DB_HOST, DB_NAME

#from backend.src.db.configs import settings



'''
Подключение к серверу
'''
#DB_URL = settings.DB_URL


DB_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
engine = create_async_engine(DB_URL, echo=True)

'''
Создание сессии для работы с БД
'''
async_session = async_sessionmaker(engine, expire_on_commit=False)

"""
Создание моделей для БД
"""

class Base(DeclarativeBase):
    pass


"""
функции создания и удаления БД
"""
async def create_database():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
