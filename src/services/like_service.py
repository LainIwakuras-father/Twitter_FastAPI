from loguru import logger

from src.utils.exception import CustomException
from utils.unitofwork import AbstractUnitOfWork


class LikeService:
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow


    async def add_like(self, tweet_id:int, current_user_id:int):
        async with self.uow:
            existing_tweet = await self.uow.tweet.find_one(id=tweet_id)
            if existing_tweet is None:
                logger.error('Твит не найден')
                raise CustomException(
                    status_code=404,
                    detail='Tweet not found'
                )

            check_existing_like = await self.uow.like.find_one(tweet_id = tweet_id, user_id=current_user_id)
            if check_existing_like:
                logger.warning("Пользователь уже ставил лайк твиту")
                raise CustomException(
                    status_code=423,
                    detail="The user has already liked this tweet"
                )

            data = dict(tweet_id=tweet_id, user_id=current_user_id)
            await self.uow.like.add_one(data)
            await self.uow.commit()
            logger.info(f"Лайк оформлен")


    async def delete_like(self, tweet_id:int, current_user_id:int):
        async with self.uow:
            existing_tweet = await self.uow.tweet.find_one(id=tweet_id)
            if existing_tweet is None:
                logger.error('Твит не найден')
                raise CustomException(
                    status_code=404,
                    detail='Tweet not found'
                )

            check_existing_like = await self.uow.like.find_one(tweet_id=tweet_id, user_id=current_user_id)
            if check_existing_like is None:
                logger.warning("Запись о лайке не найдена")
                raise CustomException(
                    status_code=423,
                    detail="The user has not yet liked this tweet"
                )

            data = dict(tweet_id=tweet_id, user_id=current_user_id)
            await self.uow.like.delete_item(**data)
            await self.uow.commit()
            logger.info(f"Дизлайк оформлен")
