from typing import List
from sqlalchemy.orm import relationship, Mapped ,mapped_column
from sqlalchemy import Table, Integer,ForeignKey, Column

from backend.src.db.db import Base
from backend.src.models.tweet import TweetOrm

#table Follow
follower_followingOrm = Table(
    'follower_following',
     Base.metadata,
    Column('follower_id', Integer, ForeignKey('user.id')),
    Column('following_id', Integer, ForeignKey('user.id'))
)


#table User
class UserOrm(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str]
    api_key:Mapped[str] = mapped_column()
    #one-to-many
    tweets: Mapped[List["TweetOrm"]] = relationship(
        backref="user", cascade="all, delete-orphan"
    )
    # one-to-many
    #likes: Mapped[List['LikeOrm']] = relationship(backref="user", cascade="all, delete-orphan")
    # many-to-many
    followers = relationship("UserOrm",
                             secondary=follower_followingOrm,
                             primaryjoin=id == follower_followingOrm.c.following_id,
                             secondaryjoin=id == follower_followingOrm.c.follower_id,
                             back_populates="following")

    following = relationship("UserOrm",
                             secondary=follower_followingOrm,
                             primaryjoin=id == follower_followingOrm.c.follower_id,
                             secondaryjoin=id == follower_followingOrm.c.following_id,
                             back_populates="followers")


    __mapper_args__ = {"confirm_deleted_rows": False}

