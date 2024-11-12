from sqlalchemy import select
from sqlalchemy.orm import selectinload
from fastapi import HTTPException

from app.db.db import async_session
from app.utils.repository import SQLAlchemyRepository


class UserSQLAlchemyRepository(SQLAlchemyRepository):
    async def find_all(self):
        async with async_session() as db:
            query = (select(self.model)
                     .options(selectinload(self.model.items))

                     )
            res = await db.execute(query)
            if res is None:
                raise HTTPException(status_code=404, detail="Ничего не найдено!")
            res = [row[0].to_read_model() for row in res.all()]
            return res

    async def find_by_id(self, id:int):
        async with async_session() as db:
            try:
                query = (select(self.model)
                         .options(selectinload(self.model.items)).
                         where(self.model.id == id)
                         )
                res = await db.execute(query)
                if res is None:
                    raise HTTPException(status_code=403, detail={'message': "user not Found!"})
                return res.scalars().one_or_none()
            except:
                raise HTTPException(status_code=403, detail={'message': "user not Found!"})