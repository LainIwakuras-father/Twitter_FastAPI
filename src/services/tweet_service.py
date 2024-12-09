from loguru import logger

from api.schemas.tweet_schema import TweetWrite, TweetRead
from src.utils.exception import CustomException
from utils.unitofwork import AbstractUnitOfWork


class TweetService:
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow


    async def add_tweet(self, tweet:TweetWrite, current_user_id: int) -> int:
        logger.debug('Добавление твита')
        tweet_dict = dict(data=tweet.data,author_id=current_user_id)
        async with self.uow:
            tweet_id = await self.uow.tweet.add_one(tweet_dict)
            tweet_media_ids = tweet.tweet_media_ids
            if tweet_media_ids and tweet_media_ids != []:
                    await self.uow.media.update_info(tweet_media_ids=tweet_media_ids, tweet_id=tweet_id)

            await self.uow.commit()
            return tweet_id


    async def get_tweets(self) -> list[TweetRead]:
       async with self.uow:
           tweets:list = await self.uow.tweet.find_all()
           return [TweetRead.model_validate(tweet) for tweet in tweets]


    async def get_tweet(self,tweet_id:int) ->TweetRead:
        async with self.uow:
            tweet = await self.uow.tweet.find_one(id=tweet_id)
            return TweetRead.model_validate(tweet)


    async def delete_tweet(self, tweet_id:int, current_user_id:int) -> bool:
        logger.debug('удаление твита')
        async with self.uow:
            existing_tweet = await self.uow.tweet.find_one(id=tweet_id)
            if existing_tweet is None:
                logger.error("Твит не найден")
                raise CustomException(status_code=404, detail="not found")
            else:
                if existing_tweet.author_id != current_user_id:
                    logger.warning("Ты удаляешь чужой твит")
                    raise CustomException(
                        status_code=423,
                        detail="The tweet that is being accessed is locked"
                    )
                else:
                    res = await self.uow.tweet.delete_item(existing_tweet)
                    await self.uow.commit()
                    return res



