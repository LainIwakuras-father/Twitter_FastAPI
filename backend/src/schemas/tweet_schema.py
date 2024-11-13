


class TweetWrite(BaseModel):
    content:str
    attachments: str
class TweetRead(TweetWrite):
     id:int
     author:'UserRead'
     likes: list['UserRead']