from  fastapi import APIRouter

likes_router = APIRouter( tags=["like"])

@likes_router.post('/tweets/{id}/likes')
async def add_like_of_tweet():
    pass

@likes_router.delete('/tweets/{id}/likes')
async def del_like_of_tweet():
    pass
