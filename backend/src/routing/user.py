from fastapi import APIRouter


user_router=APIRouter(prefix='/users',tags=['users'])

@user_router.get('/{id}')
async def get_user_id():
    pass


@user_router.get('/me')
async def get_user_me():
    pass