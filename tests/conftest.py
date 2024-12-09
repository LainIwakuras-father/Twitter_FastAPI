import asyncio
from typing import AsyncGenerator

import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from loguru import logger

from db.db import engine, Base, async_session
from src.main import app
from db.models import UserOrm
from core.configs import Settings


@pytest.fixture(scope='session', autouse=True)
async def setup_db():
    async with engine.begin() as conn:
        assert Settings.DB_NAME == 'db_test'
        await conn.run_sync(Base.metadata.create_all)
        yield
        await conn.run_sync(Base.metadata.drop_all)
        logger.info('ОЧИСТКА ТАБЛИЦЫ!')


@pytest.fixture(scope="session")
def event_loop(request):
    """
    Create an instance of the default event loop for each test case.
    """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def client() -> AsyncGenerator[AsyncClient, None]:
    """
    Асинхронный клиент для выполнения запросов
    """
    transport = ASGITransport(app=app),
    async with AsyncClient(
            transport=transport, app=app, base_url="http://localhost:8000/api"
    ) as ac:
        yield ac


@pytest.fixture(scope="session")
async def users():
    """
    Пользователи для тестирования
    """
    async with async_session() as db:
        user_1 = UserOrm(name="Даниил", api_key="key_one")
        user_2 = UserOrm(name="Ростислав", api_key="key_two")
        user_3 = UserOrm(name="Матвей", api_key="key_tree")
        user_4 = UserOrm(name="Асан", api_key="key_four")
        user_5 = UserOrm(name="Илья", api_key="key_five")
        # Подписки пользователей

        db.add_all([user_1, user_2, user_3, user_4, user_5])
        await db.commit()

        return user_1, user_2, user_3, user_4, user_5
