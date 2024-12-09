from typing import Annotated

from fastapi import APIRouter, Depends
from loguru import logger

from api.schemas.base_response import BaseGoodResponse
from api.schemas.tweet_schema import TweetWrite, TweetsOut, TweetCreateGoodResponse
from api.v1.dependencies import tweet_service, like_service
from db.models.user import UserOrm
from src.utils.get_current_user import get_current_user

tweet_router = APIRouter(prefix='/api/tweets', tags=["Tweet"])



@tweet_router.get(
    '',
        response_model=TweetsOut,
        status_code=200)
async def read_tweet(service: tweet_service):
    tweets = await service.get_tweets()
    return {'tweets': tweets}



@tweet_router.post(
    '',
        response_model=TweetCreateGoodResponse,
        status_code=201)
async def write_tweet(
        content: TweetWrite,
        current_user: Annotated[UserOrm, Depends(get_current_user)],
        service: tweet_service
):
    tweet_id = await service.add_tweet(content, current_user_id=current_user.id)
    return {'tweet_id': tweet_id}


@tweet_router.delete(
    '{id}',
    response_model=BaseGoodResponse,
    status_code=200)
async def delete_tweet(
        current_user: Annotated[UserOrm, Depends(get_current_user)],
        id: int,
        service: tweet_service
):
    await service.delete_tweet(current_user_id=current_user.id, tweet_id=id)
    return {'result': True}



@tweet_router.post(
    '/{id}/likes',
    response_model=BaseGoodResponse,
    status_code=201)
async def add_likes(
        id: int,
        current_user: Annotated[UserOrm, Depends(get_current_user)],
        service:like_service
):
    await service.add_like(tweet_id=id, current_user_id=current_user.id)
    return {'result': 'True'}



@tweet_router.delete(
    '/{id}/likes',
    response_model=BaseGoodResponse,
    status_code=200)
async def delete_likes(
        id: int,
        current_user: Annotated[UserOrm, Depends(get_current_user)],
        service: like_service
):
    await service.delete_like(tweet_id=id, current_user_id=current_user.id)
    return {'result': 'True'}
