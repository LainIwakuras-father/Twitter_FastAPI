from loguru import logger
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from db.models.likes import LikeOrm
from db.models.tweet import TweetOrm
from repositories.base_repository import SQLAlchemyRepository


class TweetRepository(SQLAlchemyRepository):
    model = TweetOrm

    async def find_all(self):
            logger.debug('просмотр ленты твитов')
            query = (select(self.model)
                     .options(
                joinedload(self.model.author),
                joinedload(self.model.likes).subqueryload(LikeOrm.user),
                joinedload(self.model.media))
                     .order_by(self.model.created_at)
                     )
            result = await self.session.execute(query)
            return result.unique().scalars().all()

    async def delete_item(self, tweet):
            await self.session.delete(tweet)




