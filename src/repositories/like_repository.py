from src.db.models.likes import LikeOrm
from src.repositories.base_repository import SQLAlchemyRepository


class LikeRepository(SQLAlchemyRepository):
    model = LikeOrm
