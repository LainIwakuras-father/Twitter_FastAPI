from pydantic import BaseModel

from src.models.user import UserOrm
from src.schemas.user_schema import UserRead


class TweetWrite(BaseModel):
    content:str
    attachments: bytes
class TweetRead(TweetWrite):
     id:int
     author:'UserRead'
     likes: list['UserRead']