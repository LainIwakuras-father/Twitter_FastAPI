from db.models.likes import LikeOrm
from repositories.base_repository import SQLAlchemyRepository


class LikeRepository(SQLAlchemyRepository):
    model = LikeOrm

