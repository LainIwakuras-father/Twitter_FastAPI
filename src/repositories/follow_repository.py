from sqlalchemy import insert

from db.models.user import follower_followingOrm
from repositories.base_repository import SQLAlchemyRepository


class FollowRepository(SQLAlchemyRepository):
    model = follower_followingOrm


    async def add_one(self, data:dict) :
            stmt = insert(self.model).values(**data)
            try:
                await self.session.execute(stmt)
                return True
            except:
                return False


