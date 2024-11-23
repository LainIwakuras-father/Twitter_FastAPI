class ImageOrm(Base):
    __tablename__ = "image"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    tweet_id:Mapped[int] = mapped_column(ForeignKey("tweet.id"))
    file_path:mapped[str]

