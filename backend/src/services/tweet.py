from loguru import logger
from sqlalchemy import insert,select
from sqlalchemy.orm import joinedload

from backend.src.db.db import async_session
from backend.src.models.tweet import TweetOrm
from backend.src.models.user import UserOrm
from backend.src.schemas.tweet_schema import TweetWrite



class TweetService:

    @classmethod
    async def add_tweet(cls,tweet_data:TweetWrite):
        logger.debug('Добавление твита')
        dict = tweet_data.model_dump()
        async  with async_session() as db:
            stmt = insert(TweetOrm).values(**dict).returning(TweetOrm.id)
            res = await db.execute(stmt)
            await db.commit()
            return res.scalar_one()

    @classmethod
    async def get_tweets(cls):
        logger.debug('просмотр ленты твитов')
        async  with async_session() as db:
            query = (select(TweetOrm)
                    .options(
                     joinedload(TweetOrm.user))
                     .order_by(TweetOrm.created_at.desc())
                     )

            result =  await db.execute(query)
            return result.unique().scalars().all()


