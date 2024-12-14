from typing import Annotated

from fastapi import Depends

from src.db.db import async_session
from src.services.follow_service import FollowService
from src.services.like_service import LikeService
from src.services.media_service import MediaService
from src.services.tweet_service import TweetService
from src.services.user_service import UserService
from src.utils.unitofwork import AbstractUnitOfWork, UnitOfWork


# НАСТРОЙКА СЕССИИ ДЛЯ МЕХАНИЗМА UNIT OF WORK
async def get_uow_with_session() -> UnitOfWork:
    return UnitOfWork(async_session)


async def get_user_service(uow: AbstractUnitOfWork = Depends(get_uow_with_session)) -> UserService:
    return UserService(uow)


async def get_tweet_service(uow: AbstractUnitOfWork = Depends(get_uow_with_session)) -> TweetService:
    return TweetService(uow)


async def get_media_service(uow: AbstractUnitOfWork = Depends(get_uow_with_session)) -> MediaService:
    return MediaService(uow)


async def get_follow_service(uow: AbstractUnitOfWork = Depends(get_uow_with_session)) -> FollowService:
    return FollowService(uow)


async def get_like_service(uow: AbstractUnitOfWork = Depends(get_uow_with_session)) -> LikeService:
    return LikeService(uow)


user_service = Annotated[UserService, Depends(get_user_service)]
tweet_service = Annotated[TweetService, Depends(get_tweet_service)]
media_service = Annotated[MediaService, Depends(get_media_service)]
follow_service = Annotated[FollowService, Depends(get_follow_service)]
like_service = Annotated[LikeService, Depends(get_like_service)]
