import pytest
from loguru import logger

from src.main import create_test_user
from tests.db_test import async_test_session
from src.db.models.user import UserOrm
from tests.db_test import engine_test,Base


@pytest.fixture(autouse=True,scope='session')
async def sturtup_event():
    """
    Удаление и создание таблиц перед тестом
    """
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

        logger.debug("TEST db created")
        yield async_test_session()



# @pytest.fixture(autouse=True,scope='session')
# async def shotdown_event():
#     yield
#     async with engine_test.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         logger.debug("Drop all")



@pytest.fixture(scope='session')
async def setup_and_teardown():
    async with async_test_session() as db:
            try:
                 user_1 = await create_test_user(db=db,name='user1',api_key='test1' )
                 user_2 = await create_test_user(db=db,name='user2',api_key='test2' )
                 user_3 = await create_test_user(db=db,name='user3',api_key='test3' )
                # Подписки пользователей
                 await db.commit()

                 logger.debug("Users created and committed.")


            except Exception as e:
                logger.error(f"Error during setup: {e}")
                raise e

            await db.commit()
            yield user_1, user_2, user_3



