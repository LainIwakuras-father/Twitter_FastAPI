from loguru import logger

from backend.src.db.db import async_session
from backend.src.models.likes import LikeOrm
from backend.src.services.tweet import TweetService
from backend.src.utils.exception import CustomException


class LikeService:
    @classmethod
    async def add_like(cls,tweet_id:int,user_id:int):
        logger.debug(f"Лайк твита №{tweet_id}")
        async  with async_session() as db:
            tweet = await TweetService.get_tweet(tweet_id=tweet_id)
            if not tweet:
                logger.error('Твит не найден')
                raise CustomException(status_code=404,detail='Tweet not found')

            like = LikeOrm(tweet_id=tweet.id,user_id=user_id)
            db.add(like)
            await db.commit()



    @classmethod
    async def delete_like(cls,tweet_id:int,user_id:int):
        logger.debug(f"Дизлайк твита №{tweet_id}")
        async  with async_session() as db:
            tweet = await TweetService.get_tweet(tweet_id=tweet_id)
            if not tweet:
                logger.error('Твит не найден')
                raise CustomException(status_code=404, detail='Tweet not found')


            db.delete()
            await db.commit()
