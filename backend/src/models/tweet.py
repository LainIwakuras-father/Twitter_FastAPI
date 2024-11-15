from datetime import datetime


from backend.src.db.db import Base
from sqlalchemy.orm import  Mapped ,mapped_column
from sqlalchemy import ForeignKey,func


"""class tweet"""
class TweetOrm(Base):
    __tablename__ = "tweet"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    data: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now(), nullable=True
    )

    __mapper_args__ = {"confirm_deleted_rows": False}