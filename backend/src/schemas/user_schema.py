from typing import Optional,List

from pydantic import BaseModel,ConfigDict


class UserWrite(BaseModel):
    name:str


class UserRead(UserWrite):

    id:int    # Автоматическое преобразование данных ORM-модели в объект схемы для сериализации
    config = ConfigDict(from_attributes=True)


class UserRel(UserRead):

    followers: Optional[List['UserRead']] = []
    following: Optional[List['UserRead']] = []

    # Автоматическое преобразование данных ORM-модели в объект схемы для сериализации
    config = ConfigDict(from_attributes=True)