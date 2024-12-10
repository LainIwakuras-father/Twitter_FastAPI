import pytest
import requests
from fastapi.testclient import TestClient

from src.api.schemas.base_response import BaseBadResponse
from src.api.schemas.base_response import BaseGoodResponse
from src.api.schemas.user_schema import UserOUT
from src.main import app
from src.utils.responces import Response


client = TestClient(app=app)

def test_get_tweets(setup_and_teardown):
    response = client.get(
        url='http://localhost:8000/api/tweets',
        headers={'api-key':'test1'}
    )
    assert response.status_code==200

    # r =  requests.get(
    #     url='http://localhost:8000/api/tweets',
    #     headers={'api-key':'test'})
    # response = Response(r)
    # response.assert_status_code(200)



def test_get_user_for_id():
    r = requests.get(
        url='http://127.0.0.1:8000/users/2',
        headers={'api-key': 'test'}
        )
    Response(r).assert_status_code(200).validate(UserOUT)


def test_get_user_me_nonheaders():
    r = requests.get(
        url='http://127.0.0.1:8000/users/2',
        )
    response = Response(r)
    response.assert_status_code(401).validate(BaseBadResponse)

def test_post_and_delete_tweet():
    r = requests.post(
        json={"tweet_data": "This is a tweet to be deleted",'tweet_media_ids':[]},
        url='http://127.0.0.1:8000/api/tweets',
        headers={'api-key':'test'})
    response = Response(r)
    response.assert_status_code(201)

    tweet_id = response.response_json["tweet_id"]
    r = requests.delete(
            f'http://localhost:8000/api/tweets/{tweet_id}',
                 headers={'api-key':'test'})
    response = Response(r)
    response.assert_status_code(200).validate(BaseGoodResponse)

def test_follow_user():
    r = requests.post(
        url='http://127.0.0.1:8000/users/2/follow',
        headers = {'api-key': 'test'}
    )
    Response(r).assert_status_code(200).validate(BaseGoodResponse)

def test_unfollow_user():
    r = requests.delete(
        url='http://127.0.0.1:8000/users/2/follow',
        headers = {'api-key': 'test'}
    )
    Response(r).assert_status_code(200).validate(BaseGoodResponse)