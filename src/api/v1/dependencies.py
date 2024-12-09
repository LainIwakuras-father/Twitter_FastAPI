from typing import Annotated

from fastapi import Depends

from services.follow_service import FollowService
from services.like_service import LikeService
from services.media_service import MediaService
from services.tweet_service import TweetService
from services.user_service import UserService
from utils.unitofwork import AbstractUnitOfWork, UnitOfWork


async def get_user_service(uow: AbstractUnitOfWork = Depends(UnitOfWork)) -> UserService:
    return UserService(uow)

async def get_tweet_service(uow: AbstractUnitOfWork = Depends(UnitOfWork)) -> TweetService:
    return TweetService(uow)

async def get_media_service(uow: AbstractUnitOfWork = Depends(UnitOfWork)) -> MediaService:
    return MediaService(uow)

async def get_follow_service(uow: AbstractUnitOfWork = Depends(UnitOfWork)) -> FollowService:
    return FollowService(uow)

async def get_like_service(uow: AbstractUnitOfWork = Depends(UnitOfWork)) -> LikeService:
    return LikeService(uow)



user_service = Annotated[UserService, Depends(get_user_service)]
tweet_service = Annotated[TweetService, Depends(get_tweet_service)]
media_service = Annotated[MediaService, Depends(get_media_service)]
follow_service = Annotated[FollowService, Depends(get_follow_service)]
like_service = Annotated[LikeService, Depends(get_like_service)]


