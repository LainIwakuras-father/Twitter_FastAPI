



class UserOrm(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    surname:Mapped[str]
    age: Mapped[int]

    items:Mapped[list['ItemOrm']]=relationship("ItemOrm",back_populates='user')

    def to_read_model(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "age": self.age,
            "items":self.items
        }