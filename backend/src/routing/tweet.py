from loguru import logger
from  fastapi import APIRouter

from backend.src.schemas.tweet_schema import TweetWrite, TweetRead
from backend.src.services.tweet import TweetService

tweet_router = APIRouter(prefix='/api/tweets',tags=["Tweet"])

@logger.catch()
@tweet_router.get('')
async def read_tweet()->list[TweetRead]:
      tweets = await TweetService.get_tweets()
      return tweets

@logger.catch()
@tweet_router.post('')
async def write_tweet(content:TweetWrite):
    tweet_id = await TweetService.add_tweet(content)
    return {'tweet_id':tweet_id}

@logger.catch()
@tweet_router.delete('{id}')
async def delete_tweet(id:int):
    pass




