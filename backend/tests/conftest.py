import asyncio
import pytest

from typing import AsyncGenerator
from httpx import AsyncClient


from backend.src.db.configs import Settings
from backend.src.db.db import engine, Base, async_session
from backend.src.main import app
from backend.src.models.user import UserOrm


@pytest.fixture(scope='session',autouse=True)
async def setup_db():
    async with engine.begin() as conn:
        print(f'{Settings.DB_NAME=}')
        await conn.run_sync(Base.metadata.create_all)
        yield
        await conn.run_sync(Base.metadata.drop_all)
        print('Все дропнулось упс!')

@pytest.fixture(scope="session")
async def users():
    """
    Пользователи для тестирования
    """
    async with async_session as db :
        user_1 = UserOrm(name="Даниил", api_key="key_one")
        user_2 = UserOrm(name="Ростислав", api_key="key_two")
        user_3 = UserOrm(name="Матвей", api_key="key_tree")
        user_4 = UserOrm(name="Асан", api_key="key_four")
        user_5 = UserOrm(name="Илья", api_key="key_five")
        # Подписки пользователей


        db.add_all([user_1, user_2, user_3, user_4, user_5])
        await db.commit()

        return user_1, user_2, user_3, user_4, user_5


@pytest.fixture(scope="session")
def event_loop(request):
    """
    Create an instance of the default event loop for each test case.
    """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()



@pytest.fixture(scope="session")
async def client() -> AsyncGenerator[AsyncClient, None]:
    """
    Асинхронный клиент для выполнения запросов
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


