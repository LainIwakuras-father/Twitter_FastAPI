import pytest
from loguru import logger
import requests

from tests.db_test import async_test_session
from src.db.models.user import UserOrm
from tests.db_test import engine_test,Base


@pytest.fixture(scope="session")
async def db():
    """
    Удаление и создание таблиц перед тестом
    """
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        logger.debug("TEST db created")
        yield async_test_session()

        logger.debug("Drop all")




@pytest.fixture(scope='function')
async def setup_and_teardown(db):
        try:
            user_1 = UserOrm(name="user1", api_key="test1")
            user_2 = UserOrm(name="user2", api_key="test2")
            user_3 = UserOrm(name="user3", api_key="test3")
        # Подписки пользователей
            user_1.following.append(user_2)
            user_2.following.append(user_1)

            db.add_all([user_1, user_2, user_3])
            await db.commit()
            logger.debug("Users created and committed.")
        except Exception as e:
            logger.error(f"Error during setup: {e}")
            raise e

        await db.commit()
        list_user = [user_1, user_2, user_3]
        yield user_1, user_2, user_3

        for user in list_user:
            db.delete(user)
        await db.commit()
        logger.debug("Users drop and committed.")