from  fastapi import APIRouter

follow_router = APIRouter( tags=["image"])

@follow_router.post('/tweets/{id}/likes')
async def add_follow():
    pass

@follow_router.delete('/tweets/{id}/likes')
async def del_follow():
    pass

