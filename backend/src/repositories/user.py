from app.models.user import UserOrm
from app.utils.user_repository import UserSQLAlchemyRepository


class UserRepository(UserSQLAlchemyRepository):
    model = UserOrm