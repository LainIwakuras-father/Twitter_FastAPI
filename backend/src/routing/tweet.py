from loguru import logger
from  fastapi import APIRouter

from backend.src.schemas.base_response import BaseGoodResponse
from backend.src.schemas.tweet_schema import TweetWrite, TweetsOut, TweetCreateGoodResponse
from backend.src.services.likes import LikeService
from backend.src.services.tweet import TweetService


tweet_router = APIRouter(prefix='/api/tweets',tags=["Tweet"])


@logger.catch()
@tweet_router.get('',response_model=TweetsOut,status_code=200)
async def read_tweet():
      tweets = await TweetService.get_tweets()
      return {'tweets':tweets}


@logger.catch()
@tweet_router.post('',response_model=TweetCreateGoodResponse,status_code=201)
async def write_tweet(content:TweetWrite):
    tweet_id = await TweetService.add_tweet(content)
    return {'tweet_id':tweet_id}


@logger.catch()
@tweet_router.delete('{id}',response_model=BaseGoodResponse)
async def delete_tweet(id:int):
    await TweetService.delete_tweet(id)
    return {'result':True}


@logger.catch()
@tweet_router.post('/{id}/likes',response_model=BaseGoodResponse,status_code=201)
async def add_likes(tweet_id:int, user_id:int):
    await LikeService.add_like(tweet_id=tweet_id, user_id=user_id)
    return {'result':'True'}


@logger.catch()
@tweet_router.delete('/{id}/likes',response_model=BaseGoodResponse,status_code=200)
async def delete_likes(tweet_id:int, user_id:int):
    await LikeService.delete_like(tweet_id=tweet_id, user_id=user_id)
    return {'result':'True'}
