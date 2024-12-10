from loguru import logger

from src.utils.exception import CustomException
from src.utils.unitofwork import AbstractUnitOfWork


class FollowService:
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow

    async def add_follow(self, current_user_id: int, following_id: int):
        logger.debug(f'пользователь с id:{current_user_id} пытается подписыватся на пользователя с id:{following_id}')
        async with self.uow:
            following_user = await self.uow.user.find_one(id=following_id)
            if following_user is None:
                logger.error(
                    f"Не найден пользователь(id: {following_user})"
                )
                raise CustomException(
                    status_code=404,
                    detail='Not found user'
                )

            if current_user_id == following_id:
                logger.error("Невалидные данные - попытка подписаться на самого себя")
                raise CustomException(
                    status_code=422,
                    detail="Invalid data. You can't subscribe to yourself"
                )

            existing_follow = await self.uow.follow.find_one(follower_id=current_user_id, following_id=following_id)
            if existing_follow:
                logger.warning(f"Подписка уже оформлена")
                raise CustomException(
                    status_code=423,
                    detail="The user is already subscribed"
                )

            data = dict(follower_id=current_user_id, following_id=following_id)
            res = await self.uow.follow.add_one(data)
            await self.uow.commit()
            logger.info(f"Подписка оформлена")
            return res

    async def unfollow(self, current_user_id, following_id):
        async with self.uow:
            logger.debug(
                f'пользователь с id:{current_user_id} пытается отписыватся от пользователя с id:{following_id}')
            following_user = await self.uow.user.find_one(id=following_id)
            if following_user is None:
                logger.error(
                    f"Не найден пользователь(id: {following_user})"
                )
                raise CustomException(
                    status_code=404,
                    detail='Not found user'
                )

            if current_user_id == following_id:
                logger.error("Невалидные данные - попытка отписаться от самого себя")
                raise CustomException(
                    status_code=422,
                    detail="Invalid data. You can't unsubscribe to yourself"
                )

            existing_follow = await self.uow.follow.find_one(follower_id=current_user_id, following_id=following_id)
            if not existing_follow:
                logger.warning(f"Подписка не обнаружена")
                raise CustomException(
                    status_code=423,
                    detail="The user is not among the subscribers"
                )
            data = dict(follower_id=current_user_id, following_id=following_id)
            res = await self.uow.follow.delete_item(**data)
            await self.uow.commit()
            logger.info(f"Отписка оформлена")
            return res
