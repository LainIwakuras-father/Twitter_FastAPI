from typing import Annotated

from fastapi import APIRouter, Depends
from loguru import logger

from src.models.user import UserOrm
from src.schemas.base_response import BaseGoodResponse
from src.schemas.user_schema import UserOUT
from src.services.follow import FollowService
from src.services.user import UserService
from src.utils.get_current_user import get_current_user

user_router = APIRouter(prefix='/users', tags=['users'])


@user_router.get('/me', response_model=UserOUT, status_code=200)
async def get_user_me(current_user: Annotated[UserOrm, Depends(get_current_user)]):
    return {'user': current_user}


@user_router.get('/{id}', response_model=UserOUT, status_code=200)
async def get_user_id(id: int):
    user = await UserService.get_user_for_id(id)
    return {'user': user}


@logger.catch()
@user_router.post('/{id}/follow', response_model=BaseGoodResponse, status_code=200)
async def following_user(current_user: Annotated[UserOrm, Depends(get_current_user)]
                         , following_id: int):
    try:
        await FollowService.add_follow(user_id=current_user.id, following_id=following_id)
        return {'result': 'True'}
    except:
        return {'result': 'False'}


@logger.catch()
@user_router.delete('/{id}/follow', response_model=BaseGoodResponse, status_code=200)
async def delete_following_user(current_user: Annotated[UserOrm, Depends(get_current_user)]
                                , following_id: int):
    await FollowService.unfollow(current_user_id=current_user.id, following_id=following_id)
    return {'result': 'True'}
