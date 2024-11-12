from itertools import product
from typing import Annotated

from fastapi import APIRouter, Depends
from app.api.dependencies import user_service
from app.schemas.user_schema import UserWrite

from app.services.user import UserService

user_router=APIRouter(prefix='/users',tags=['users'])


@user_router.get("")
async def users_read(service: Annotated[UserService,Depends(user_service)]):
    users = await service.get_users()
    return {'users':users}


@user_router.post("/userAdd")
async def user_create(
        user_data: UserWrite,
        service: Annotated[UserService,Depends(user_service)]
        ):
    user_id = await service.add_user(user_data)
    return {'user_id':user_id}


@user_router.get("/{id}")
async def user_read(
        id:int,
        service: Annotated[UserService,Depends(user_service)]
        )->dict:
    user = await service.get_user_info(id)
    return {'user':user}


@user_router.delete('/deleteUser')
async def delete_user(
        id:int,
        service: Annotated[UserService,Depends(user_service)]
        )->str:
    res = await service.delete_user(id)
    return res

