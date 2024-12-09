from datetime import datetime
from typing import List

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db import Base
from db.models.likes import LikeOrm
from db.models.media import MediaOrm

"""class tweet"""


class TweetOrm(Base):
    __tablename__ = "tweet"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    data: Mapped[str] = mapped_column(index=True)
    media: Mapped[List[MediaOrm]] = relationship('MediaOrm', back_populates='tweet', cascade="all, delete-orphan")

    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    author = relationship('UserOrm', back_populates='tweets')
    likes: Mapped[List['LikeOrm']] = relationship('LikeOrm', back_populates='tweet', cascade="all, delete-orphan")

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now(), nullable=True
    )

    __mapper_args__ = {"confirm_deleted_rows": False}

    # def to_read_model(self) -> TweetRead:
    #     return TweetRead(
    #         id=self.id,
    #         data=self.data,
    #         media=self.media,
    #         author=self.author,
    #         likes=self.likes
    #     )