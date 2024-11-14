from datetime import datetime
from typing import List

from backend.src.db.db import Base
from sqlalchemy.orm import relationship, Mapped ,mapped_column
from sqlalchemy import ForeignKey



class TweetOrm(Base):
    __tablename__ = "tweet"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    data: Mapped[str]
    #tweet-images
    # attachments: Mapped[List['ImageOrm']] = relationship(backref="tweet", cascade="all, delete-orphan")
    #user-tweet
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    author = relationship(backref="tweet")
    #tweet-likes
    # likes: Mapped[List['LikeOrm']] = relationship(backref="tweet", cascade="all, delete-orphan")

    created_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow, nullable=True
    )