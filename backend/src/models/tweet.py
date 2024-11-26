from datetime import datetime

from typing import List

from backend.src.db.db import Base
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey,func

from backend.src.models.media import MediaOrm
from backend.src.models.likes import LikeOrm

"""class tweet"""
class TweetOrm(Base):
    __tablename__ = "tweet"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    data: Mapped[str] = mapped_column(index=True)
    media: Mapped[List[MediaOrm]] = relationship('MediaOrm',back_populates='tweet', cascade="all, delete-orphan")

    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    author = relationship('UserOrm',back_populates='tweets')
    likes: Mapped[List['LikeOrm']] = relationship('LikeOrm', back_populates='tweet', cascade="all, delete-orphan")

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now(), nullable=True
    )

    __mapper_args__ = {"confirm_deleted_rows": False}