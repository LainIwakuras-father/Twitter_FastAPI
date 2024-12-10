from loguru import logger
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.db.models.user import UserOrm
from src.repositories.base_repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = UserOrm

    async def find_one(self, **filter_by):
        """классический шаблон кода метода для эндпоинтов для работы с БД"""
        logger.debug(f"Поиск пользователя по {filter_by}")
        query = (select(self.model)
                 .filter_by(**filter_by)
                 .options(selectinload(self.model.following),
                          selectinload(self.model.followers))
                 )
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
