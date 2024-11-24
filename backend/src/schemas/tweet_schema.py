from typing import List, Optional

from pydantic import BaseModel, Field, ConfigDict, model_validator

from backend.src.schemas.base_response import BaseGoodResponse
from backend.src.schemas.user_schema import User


class Like(BaseModel):
      id:int = Field(alias='user_id')
      user: str = Field(alias='name')
      model_config = ConfigDict(from_attributes=True, populate_by_name=True)

      @model_validator(mode="before")
      def extract_user(cls, data):
            """
            Метод извлекает и возвращает данные о пользователе из объекта Like
            """
            # ВАЖНО: доступ к данным пользователя возможен благодаря связыванию данных при SQL-запросе к БД
            # при выводе твитов - joinedload(Tweet.likes).subqueryload(Like.user)
            user = data.user
            return user


class MediaOutTweet(BaseModel):
      file_path:str
      model_config = ConfigDict(from_attributes=True)

class Media:
      id:int
      file_path:str
      #model_config = ConfigDict(from_attributes=True)

class MediaOut(BaseGoodResponse):
      id:int = Field(alias='media_id')
      model_config = ConfigDict(from_attributes=True, populate_by_name=True)



class TweetWrite(BaseModel):
      data: str = Field()
      tweet_media_ids: Optional[List[int]]
      author_id:int

      model_config = ConfigDict(from_attributes=True,populate_by_name=True)


class TweetRead(BaseModel):
      id:int
      data:str = Field(alias='content')
      media: List[str] = Field('attachments')
      author:User
      likes:Optional[List['Like']] = []
      model_config = ConfigDict(from_attributes=True,populate_by_name=True)

#СХЕМА ВЫВОДА СПИСКА ТВИТОВ
class TweetsOut(BaseGoodResponse):
      tweets:List[TweetRead]