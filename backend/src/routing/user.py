from fastapi import APIRouter


from backend.src.schemas.user_schema import UserRel
from backend.src.services.user import UserService

user_router=APIRouter(prefix='/users',tags=['users'])

@user_router.get('/{id}', response_model=UserRel)
async def get_user_id(id: int)->UserRel:
    user = await UserService.get_user_for_id(id)
    return user

@user_router.get('/me')
async def get_user_me():
    pass

