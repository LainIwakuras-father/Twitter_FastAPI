from abc import ABC ,abstractmethod

from fastapi import HTTPException
from sqlalchemy import insert, select, update, delete

from app.db.db import async_session


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self,data):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError

    @abstractmethod
    async def find_by_id(self,id):
        raise NotImplementedError

    @abstractmethod
    async def update_info(self,id,data):
        raise NotImplementedError

    @abstractmethod
    async def delete_item(self, id):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self,data):
        async  with async_session() as db:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await db.execute(stmt)
            await db.commit()
            return res.scalar_one()

    async def find_by_id(self,id:int):
        async with async_session() as db:
            query=select(self.model).where(self.model.id==id)
            res = await db.execute(query)
            return res.scalar_one_or_none()

    async def find_all(self):
        async with async_session() as db:
            query = select(self.model)
            res = await db.execute(query)
            res = [row[0].to_read_model for row in res.all()]
            return res

    async  def update_info(self, id:int, data:dict):
        async  with async_session() as db:
            stmt = select(self.model).where(self.model.id == id)
            result = await db.execute(stmt)
            product = result.scalar_one_or_none()

            if product is None:
                raise HTTPException(status_code=404, detail="not found")

            stmt = update(self.model).where(self.model.id == id).values(**data)

            await db.execute(stmt)
            await db.commit()
            return "Success"

    async def delete_item(self, id:int):
        async with async_session() as db:
            existing_task = await db.get(self.model,id)
            if existing_task is None:
                raise HTTPException(status_code=404, detail="not found")
            await db.delete(existing_task)
            await db.commit()
            return 'Success'






