from abc import ABC, abstractmethod

from src.db.db import async_session
from src.repositories.follow_repository import FollowRepository
from src.repositories.like_repository import LikeRepository
from src.repositories.media_repository import MediaRepository
from src.repositories.tweet_repository import TweetRepository
from src.repositories.user_repository import UserRepository


class AbstractUnitOfWork(ABC):
    user: UserRepository
    tweet: TweetRepository
    follow: FollowRepository
    like: LikeRepository
    media: MediaRepository

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, *args):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork(AbstractUnitOfWork):
    def __init__(self, session=async_session):
        self.session_factory = session

    async def __aenter__(self):
        self.session = self.session_factory()

        self.user = UserRepository(self.session)
        self.tweet = TweetRepository(self.session)
        self.follow = FollowRepository(self.session)
        self.like = LikeRepository(self.session)
        self.media = MediaRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
