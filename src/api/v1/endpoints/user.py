from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.schemas.base_response import BaseGoodResponse
from src.api.schemas.user_schema import UserOUT
from src.api.v1.dependencies import user_service, follow_service
from src.db.models.user import UserOrm
from src.utils.get_current_user import get_current_user

user_router = APIRouter(prefix='/users', tags=['users'])


@user_router.get('/me', response_model=UserOUT, status_code=200)
async def get_user_me(current_user: Annotated[UserOrm, Depends(get_current_user)]):
    return {'user': current_user}


@user_router.get(
    '/{id}',
    response_model=UserOUT,
    status_code=200)
async def get_user_id(
        id: int,
        service: user_service):
    user = await service.get_for_id(id)
    return {'user': user}


@user_router.post(
    '/{id}/follow',
    response_model=BaseGoodResponse,
    status_code=200)
async def following_user(
        current_user: Annotated[UserOrm, Depends(get_current_user)]
        , id: int
        , service: follow_service
):
    res = await service.add_follow(current_user_id=current_user.id, following_id=id)
    return {'result': res}


@user_router.delete(
    '/{id}/follow',
    response_model=BaseGoodResponse,
    status_code=200)
async def delete_following_user(
        current_user: Annotated[UserOrm, Depends(get_current_user)]
        , id: int
        , service: follow_service
):
    await service.unfollow(current_user_id=current_user.id, following_id=id)
    return {'result': 'True'}
