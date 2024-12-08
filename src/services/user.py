from loguru import logger
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.db import async_session
from src.models.user import UserOrm


class UserService:
    # service user get current_user and get_for id
    @classmethod
    async def get_user_for_id(cls, id: int) -> UserOrm | None:
        async with async_session() as db:
            """классический шаблон кода метода для эндпоинтов для работы с БД"""
            logger.debug(f"Поиск пользователя по id: {id}")

            query = (select(UserOrm)
                     .where(UserOrm.id == id)
                     .options(selectinload(UserOrm.following),
                              selectinload(UserOrm.followers))
                     )
            result = await db.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_user_for_me(cls, api_key: str) -> UserOrm | None:
        async with async_session() as db:
            logger.debug(f"Поиск пользователя по api-key: {api_key}")
            query = (select(UserOrm)
                     .where(UserOrm.api_key == api_key)
                     .options(selectinload(UserOrm.following),
                              selectinload(UserOrm.followers))
                     )
            result = await db.execute(query)
            return result.scalar_one_or_none()
