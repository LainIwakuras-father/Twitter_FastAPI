from abc import ABC, abstractmethod

from loguru import logger
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from utils.exception import CustomException


class AbstractRepository(ABC):



    @abstractmethod
    async def add_one(self, data):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError

    @abstractmethod
    async def find_one(self):
        raise NotImplementedError

    @abstractmethod
    async def update_info(self, id, data):
        raise NotImplementedError

    @abstractmethod
    async def delete_item(self, **filter_by):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data:dict) -> int:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await self.session.execute(stmt)
            return res.scalar_one()

    async def find_one(self, **filter_by):
            logger.debug(f"Поиск  по : {filter_by}")
            query = select(self.model).filter_by(**filter_by)
            res = await self.session.execute(query)
            return res.scalar_one_or_none()


    async def find_all(self):
            query = select(self.model)
            res = await self.session.execute(query)
            return res.scalars().all()

    async  def update_info(self, id:int, data:dict):
            stmt = update(self.model).values(**data).filter_by(id=id)
            await self.session.execute(stmt)
            return True

    async def delete_item(self, **filter_by):
            stmt = (delete(self.model).filter_by(**filter_by))
            await self.session.execute(stmt)
            return True