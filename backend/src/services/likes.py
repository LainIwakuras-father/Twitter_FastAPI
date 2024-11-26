from loguru import logger
from sqlalchemy import select

from backend.src.db.db import async_session
from backend.src.models.likes import LikeOrm
from backend.src.services.tweet import TweetService
from backend.src.utils.exception import CustomException


class LikeService:
    @classmethod
    async def check_existing_like(cls,tweet_id:int,user_id:int)->LikeOrm|None:
        logger.debug("Поиск записи о лайке")
        async  with async_session() as db:
            query = (select(LikeOrm)
                    .where(
                    LikeOrm.tweet_id==tweet_id,
                    LikeOrm.user_id==user_id)
            )
            like = await db.execute(query)
            return like.scalar_one_or_none()


    @classmethod
    async def add_like(cls,tweet_id:int,user_id:int) ->None:
        logger.debug(f"Лайк твита №{tweet_id}")
        async  with async_session() as db:
            tweet = await TweetService.get_tweet(tweet_id=tweet_id)
            if not tweet:
                logger.error('Твит не найден')
                raise CustomException(
                    status_code=404,
                    detail='Tweet not found'
                )
            if await cls.check_existing_like(tweet_id=tweet_id, user_id=user_id):
                logger.warning("Пользователь уже ставил лайк твиту")
                raise CustomException(
                    status_code=423,
                    detail="The user has already liked this tweet"
                )

            like = LikeOrm(tweet_id=tweet_id,user_id=user_id)
            db.add(like)
            await db.commit()


    @classmethod
    async def delete_like(cls,tweet_id:int,user_id:int)->None:
        logger.debug(f"Дизлайк твита №{tweet_id}")
        async  with async_session() as db:
            existing_tweet = await TweetService.get_tweet(tweet_id=tweet_id)
            if existing_tweet is None:
                logger.error('Твит не найден')
                raise CustomException(
                    status_code=404,
                    detail='Tweet not found'
                )

            existing_like = await cls.check_existing_like(tweet_id=existing_tweet.id,user_id=user_id)
            if  existing_like is None:
                logger.warning("Запись о лайке не найдена")
                raise CustomException(
                    status_code=423,
                    detail="The user has not yet liked this tweet"
                )
            await db.delete(existing_like)
            await db.commit()
