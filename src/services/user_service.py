from src.api.schemas.user_schema import UserFromDB
from src.utils.exception import CustomException
from src.utils.unitofwork import AbstractUnitOfWork


class UserService:
    # service user get current_user and get_for id
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow

    async def get_for_id(self, id: int) -> UserFromDB:
        async with self.uow:
            user = await self.uow.user.find_one(id=id)
            if user is None:
                raise CustomException(status_code=404, detail="not found")
            else:
                return UserFromDB.model_validate(user)

    async def get_for_apikey(self, api_key: str) -> UserFromDB:
        async with self.uow:
            user = await self.uow.user.find_one(api_key=api_key)
            return UserFromDB.model_validate(user)
