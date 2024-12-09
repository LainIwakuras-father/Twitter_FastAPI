from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db import Base


class MediaOrm(Base):
    __tablename__ = "media"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    tweet_id: Mapped[int] = mapped_column(ForeignKey("tweet.id"), nullable=True)
    file_path: Mapped[str] = mapped_column(index=True)
    tweet = relationship('TweetOrm', back_populates='media')

    __mapper_args__ = {"confirm_deleted_rows": False}
