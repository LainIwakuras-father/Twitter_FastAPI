from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.api.dependencies import get_uow_with_session
from src.main import app
from src.db.db import Base
from src.core.configs import Settings
from src.utils.unitofwork import UnitOfWork

'''
Подключение к тестовому серверу
'''
DB_URL_TEST = Settings.DB_URL
engine_test = create_async_engine(DB_URL_TEST, poolclass=NullPool)
'''
Создание сессии для работы с БД
'''
async_test_session = async_sessionmaker(
    engine_test, expire_on_commit=False, class_=AsyncSession
)
"""
Создание моделей для БД
"""
Base.metadata.bind = engine_test

async def test_get_uow_with_session() -> UnitOfWork:
    return UnitOfWork(async_test_session)

"""
1) в файле pytest.ini я переопределил файл .env на .test.env
2) здесь я созданную тестовую сессию переопределил в мое приложение
"""
app.dependency_overrides[get_uow_with_session]=test_get_uow_with_session

