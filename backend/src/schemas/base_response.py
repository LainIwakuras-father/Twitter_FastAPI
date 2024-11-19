from pydantic import BaseModel

#схема вывода сообщений с кодом 200
class BaseGoodResponse(BaseModel):
    result:bool=True