from pydantic import BaseModel


class UserWrite(BaseModel):
    name:str

class UserRead(UserWrite):
    id:int

class UserRel(UserRead):
    followers:list['UserRead']
    following:list['UserRead']