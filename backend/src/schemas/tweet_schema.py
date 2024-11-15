from pydantic import BaseModel,Field,ConfigDict

from backend.src.schemas.user_schema import User


class TweetWrite(BaseModel):
      data: str = Field()
      author_id:int
      model_config = ConfigDict(from_attributes=True)


class TweetRead(BaseModel):
      id:int
      tweet_data:str = Field(alias='content')
      author:User
      model_config = ConfigDict(from_attributes=True,populate_by_name=True)