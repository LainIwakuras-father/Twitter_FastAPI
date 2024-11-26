from typing import Annotated
from loguru import logger
from fastapi import APIRouter, Depends


from backend.src.models.user import UserOrm
from backend.src.schemas.base_response import BaseGoodResponse
from backend.src.schemas.user_schema import  UserOUT
from backend.src.services.follow import FollowService
from backend.src.services.user import UserService
from backend.src.utils.get_current_user import get_current_user

user_router=APIRouter(prefix='/users',tags=['users'])



@user_router.get('/{id}', response_model=UserOUT,status_code=200)
async def get_user_id(id: int ):
    user = await UserService.get_user_for_id(id)
    return  {'user':user}



@user_router.get('/users/me',response_model=UserOUT,status_code=200)
async def get_user_me(current_user:Annotated[UserOrm,Depends(get_current_user)]):
    return {'user': current_user}


@logger.catch()
@user_router.post('/{id}/follow',response_model=BaseGoodResponse,status_code=200)
async def following_user(current_user:Annotated[UserOrm,Depends(get_current_user)]
                         ,following_id:int):

    await FollowService.add_follow(user_id=current_user.id, following_id=following_id)

    return {'result':'True'}


@logger.catch()
@user_router.delete('/{id}/follow',response_model=BaseGoodResponse,status_code=200)
async def delete_following_user(current_user:Annotated[UserOrm,Depends(get_current_user)]
                         ,following_id:int):
    await FollowService.unfollow(current_user_id=current_user.id,following_id=following_id)
    return {'result':'True'}