from fastapi import Depends
from fastapi import Security
from fastapi.requests import Request
from fastapi.security import APIKeyHeader
from loguru import logger

from api.v1.dependencies import get_user_service
from services.user_service import UserService
from src.utils.exception import CustomException


class APITokenKeyHeader(APIKeyHeader):
    """
    извлечение api-key
    """

    async def __call__(self, request: Request) -> str | None:
        api_key = request.headers.get(self.model.name)

        if api_key is None:
            if self.auto_error:
                raise CustomException(
                    status_code=401,
                    detail='User authorization error'
                )
            else:
                return None

        return api_key


'''
запрос для записи api-key
а Security = окно 
'''
query_api_key = APITokenKeyHeader(name="api-key")


async def get_current_user(
        api_key: str = Security(query_api_key),
        service: UserService = Depends(get_user_service)
) :

    '''
        функция проверки текущего пользователя
    '''

    if api_key is None:
        logger.error("Токен не найден в header")
        raise CustomException(
            status_code=401,
            detail="Valid api-token token is missing"
        )

    current_user = await service.get_for_apikey(api_key=api_key)
    if current_user is None:
        raise CustomException(
            status_code=401,
            detail="Sorry. Wrong api-key token. This user does not exist"
        )
    return current_user
