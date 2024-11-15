from fastapi import HTTPException

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from backend.src.db.db import async_session
from backend.src.models.user import UserOrm
from backend.src.schemas.user_schema import UserRel


class UserService:
#service user get current_user and get_for id
    @classmethod
    async def get_user_for_id(cls,id:int)->UserRel| None:
             async with async_session() as db:
                 query = select(UserOrm).where(UserOrm.id==id).options(selectinload(UserOrm.following),selectinload(UserOrm.followers))
                 if query is None:
                     raise HTTPException(status_code=404, detail="User not found")
                 result = await db.execute(query)
                 return result.scalar_one_or_none()


    @classmethod
    async def get_user_for_me(cls,token:str):
                 async with async_session() as db:
                     query = select(UserOrm).where(UserOrm.api_key==token).options(selectinload(UserOrm.following),selectinload(UserOrm.followers))
                     result = await db.execute(query)
                     return result.scalar_one_or_none()