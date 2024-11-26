from typing import Annotated

from loguru import logger
from  fastapi import APIRouter,Depends

from backend.src.models.user import UserOrm
from backend.src.schemas.base_response import BaseGoodResponse
from backend.src.schemas.tweet_schema import TweetWrite, TweetsOut, TweetCreateGoodResponse
from backend.src.services.likes import LikeService
from backend.src.services.tweet import TweetService
from backend.src.utils.get_current_user import get_current_user

tweet_router = APIRouter(prefix='/api/tweets',tags=["Tweet"])


@logger.catch()
@tweet_router.get('',response_model=TweetsOut,status_code=200)
async def read_tweet():
      tweets = await TweetService.get_tweets()
      return {'tweets':tweets}


@logger.catch()
@tweet_router.post('',response_model=TweetCreateGoodResponse,status_code=201)
async def write_tweet(content:TweetWrite,
                      current_user:Annotated[UserOrm,Depends(get_current_user)]):
    tweet_id = await TweetService.add_tweet(content,current_user_id=current_user.id)
    return {'tweet_id':tweet_id}



@tweet_router.delete('{id}',response_model=BaseGoodResponse,status_code=200)
async def delete_tweet(current_user:Annotated[UserOrm,Depends(get_current_user)],
                       tweet_id:int
                       ):
    await TweetService.delete_tweet(current_user_id=current_user.id,tweet_id=tweet_id)
    return {'result':True}


@logger.catch()
@tweet_router.post('/{id}/likes',response_model=BaseGoodResponse,status_code=201)
async def add_likes(tweet_id:int, current_user:Annotated[UserOrm,Depends(get_current_user)]):
    await LikeService.add_like(tweet_id=tweet_id, user_id=current_user.id)
    return {'result':'True'}


@logger.catch()
@tweet_router.delete('/{id}/likes',response_model=BaseGoodResponse,status_code=200)
async def delete_likes(tweet_id:int,current_user:Annotated[UserOrm,Depends(get_current_user)]):
    await LikeService.delete_like(tweet_id=tweet_id, user_id=current_user.id)
    return {'result':'True'}
