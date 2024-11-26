from loguru import logger

from fastapi import Security
from fastapi.requests import Request
from fastapi.security import APIKeyHeader

from backend.src.models.user import UserOrm
from backend.src.services.user import UserService
from backend.src.utils.exception import CustomException


class APITokenKeyHeader(APIKeyHeader):
        """
        извлечение api-key
        """
        async def __call__(self,request:Request) -> str|None:
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

async def get_current_user(api_key:str = Security(query_api_key))->UserOrm|None:

        '''
            функция проверки текущего пользователя
        '''
        if api_key is None:
                logger.error("Токен не найден в header")
                raise CustomException(
                        status_code=401,
                        detail="Valid api-token token is missing"
                )

        current_user = await UserService.get_user_for_me(api_key)
        if current_user is None:
                raise CustomException(
                        status_code=401,
                        detail="Sorry. Wrong api-key token. This user does not exist"
                )
        return current_user









