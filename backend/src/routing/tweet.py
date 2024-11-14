from  fastapi import APIRouter

tweet_router = APIRouter(tags=["Tweet"])

@tweet_router.get('/api/tweets')
async def read_tweet():
    pass

@tweet_router.post('/api/tweets')
async def write_tweet():
    pass

@tweet_router.delete('/api/tweets/{id}')
async def delete_tweet():
    pass




