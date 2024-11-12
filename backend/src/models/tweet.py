

class TweetOrm(Base):
    __tablename__ = 'tweet'
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str]
    attachments:Mapped[list[bytes]]


    author_id: Mapped[int]=mapped_column(ForeignKey("user.id",ondelete='CASCADE'))
    author:Mapped['UserOrm'] = relationship("UserOrm",back_populates='items')

    likes: Mapped[list[LikeOrm]] =