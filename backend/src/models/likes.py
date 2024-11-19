from datetime import datetime

from sqlalchemy.orm import  Mapped ,mapped_column ,relationship
from sqlalchemy import ForeignKey,func

from backend.src.db.db import Base



class LikeOrm(Base):
    __tablename__ = "like"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    tweet_id:Mapped[int] = mapped_column(ForeignKey("tweet.id"))
    user_id:Mapped[int] = mapped_column(ForeignKey("user.id"))

    user = relationship('UserOrm',back_populates='likes')
    tweet = relationship('TweetOrm',back_populates='likes')

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now(), nullable=True
    )


