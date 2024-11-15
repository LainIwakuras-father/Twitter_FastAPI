from typing import Optional,List

from pydantic import BaseModel,ConfigDict


class UserWrite(BaseModel):
    name:str
    model_config= ConfigDict(from_attributes=True)


class User(BaseModel):
    id:int
    name:str


class UserRel(User):

    followers: Optional[List['User']] = []
    following: Optional[List['User']] = []

    # Автоматическое преобразование данных ORM-модели в объект схемы для сериализации
    model_config = ConfigDict(from_attributes=True)
    #old method
    # class Config:
    #     orm_mode = True