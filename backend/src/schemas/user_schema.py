from typing import Optional,List

from pydantic import BaseModel,ConfigDict

from backend.src.schemas.base_response import BaseGoodResponse


class UserWrite(BaseModel):
    name:str
    model_config= ConfigDict(from_attributes=True)


class User(BaseModel):
    id:int
    name:str
    model_config = ConfigDict(from_attributes=True)

class UserRel(User):

    followers: Optional[List['User']] = []
    following: Optional[List['User']] = []

    # Автоматическое преобразование данных ORM-модели в объект схемы для сериализации

    #old method
    # class Config:
    #     orm_mode = True

class UserOUT(BaseGoodResponse):
    user:UserRel