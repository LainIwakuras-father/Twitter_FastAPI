from loguru import logger
from sqlalchemy import insert,delete

from backend.src.db.db import async_session
from backend.src.models.user import UserOrm, follower_followingOrm
from backend.src.services.user import UserService
from backend.src.utils.exception import CustomException


class FollowService:
    @classmethod
    async def add_follow(cls, user_id:int, following_id:int) -> None:
        logger.debug(f'пользователь с id:{user_id} пытается подписыватся на пользователя с id:{following_id}')
        async  with async_session() as db:
             user_db = await UserService.get_user_for_id(id=user_id)
             if not user_db:
                 logger.error(
                     f"Не найден пользователь(id: {user_id})"
                 )
                 raise CustomException(
                     status_code=404,
                     detail='Not found user'
                 )

             following_user = await UserService.get_user_for_id(id=following_id)
             if not following_user:
                logger.error(
                    f"Не найден пользователь(id: {following_user})"
                )
                raise CustomException(
                    status_code=404,
                    detail='Not found user'
                )

             if user_id == following_id:
                logger.error("Невалидные данные - попытка подписаться на самого себя")
                raise CustomException(
                    status_code=422,
                    detail="Invalid data. You can't subscribe to yourself"
                )

             if await cls.check_follower(user_db,following_id):
                 logger.warning(f"Подписка уже оформлена")
                 raise CustomException(
                     status_code=423,
                     detail="The user is already subscribed"
                 )

             stmt = insert(follower_followingOrm).values(follower_id=user_id,following_id=following_id)
             await db.execute(stmt)
             await db.commit()
             logger.info(f"Подписка оформлена")


    @classmethod
    async def check_follower(cls, current_user: UserOrm, following_user_id: int) -> bool:
        return following_user_id in [
            following.id for following in current_user.following
        ]

    @classmethod
    async def unfollow(cls, current_user_id:int,following_id:int)->None:
        logger.debug(f'пользователь с id:{current_user_id} пытается отписыватся от пользователя с id:{following_id}')
        async with async_session() as db:
            current_user = await UserService.get_user_for_id(id=current_user_id)
            if not current_user:
                logger.error(
                    f"Не найден пользователь(id: {current_user_id})"
                )
                raise CustomException(
                    status_code=404,
                    detail='Not found user')

            following_user = await UserService.get_user_for_id(id=following_id)
            if not following_user:
                logger.error(
                    f"Не найден пользователь(id: {following_user})"
                )
                raise CustomException(
                    status_code=404,
                    detail='Not found user')

            if current_user_id == following_id:
                logger.error("Невалидные данные - попытка отписаться от самого себя")
                raise CustomException(
                    status_code=422,
                    detail="Invalid data. You can't unsubscribe to yourself")

            if not await cls.check_follower(current_user=current_user,following_user_id=following_user.id):
                logger.warning(f"Подписка не обнаружена")
                raise CustomException(
                    status_code=423,
                    detail="The user is not among the subscribers"
                )
            stmt = (delete(follower_followingOrm)
                    .where(follower_followingOrm.c.follower_id==current_user_id,
                           follower_followingOrm.c.following_id==following_id
                           )
            )
            await db.execute(stmt)
            await db.commit()
        logger.info(f"Отписка оформлена")