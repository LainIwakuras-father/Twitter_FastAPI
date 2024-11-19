from loguru import logger
from fastapi import APIRouter

from backend.src.schemas.base_response import BaseGoodResponse
from backend.src.schemas.user_schema import UserRel, UserOUT
from backend.src.services.follow import FollowService
from backend.src.services.user import UserService


user_router=APIRouter(prefix='/users',tags=['users'])


@logger.catch()
@user_router.get('/{id}', response_model=UserOUT,status_code=200)
async def get_user_id(id: int):
    user = await UserService.get_user_for_id(id)
    return  {'user':user}


@logger.catch()
@user_router.get('/me')
async def get_user_me():
    pass


@logger.catch()
@user_router.post('/{id}/follow',response_model=BaseGoodResponse,status_code=200)
async def following_user(user_id:int,following_id:int):
    await FollowService.add_follow(user_id=user_id, following_id=following_id)
    return {'result':'True'}


@logger.catch()
@user_router.delete('/{id}/follow',response_model=BaseGoodResponse,status_code=200)
async def delete_following_user(id:int):
    await FollowService.delete_follow(id)
    return {'result':'True'}