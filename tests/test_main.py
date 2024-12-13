import pytest
from fastapi.testclient import TestClient

from src.api.schemas.base_response import BaseBadResponse
from src.api.schemas.base_response import BaseGoodResponse
from src.api.schemas.user_schema import UserOUT
from src.main import app
from src.utils.responces import Response


client = TestClient(app=app)


def test_get_tweets(setup_and_teardown):
    response = client.get(
        url='http://127.0.0.1:8000/api/tweets',
        headers={'api-key':'test1'}
    )
    assert response.status_code==200

    # r =  requests.get(
    #     url='http://localhost:8000/api/tweets',
    #     headers={'api-key':'test'})
    # response = Response(r)
    # response.assert_status_code(200)



def test_get_user_for_id(setup_and_teardown):
    test_user, test_user2, test_user3= setup_and_teardown
    r = client.get(
        url='http://127.0.0.1:8000/users/2',
        headers={'api-key': 'test1'}
        )
    assert r.status_code==200

    #Response(r).assert_status_code(200).validate(UserOUT)


def test_get_user_me_nonheaders(setup_and_teardown):
    r = client.get(
        url='http://127.0.0.1:8000/users/2',
        )
    assert r.status_code==401
    #response = Response(r)
    #response.assert_status_code(401).validate(BaseBadResponse)

#class TestTweet:
def test_post_and_delete_tweet_and_like():
    r = client.post(
        json={"tweet_data": "This is a tweet to be deleted",'tweet_media_ids':[]},
        url='http://localhost:8000/api/tweets',
        headers={'api-key':'test1'})
    assert r.status_code==201
    tweet_id = r.json()["tweet_id"]
    #response = Response(r)
    #response.assert_status_code(201)

    responce = client.post(
        url=f'http://localhost:8000/api/tweets/{tweet_id}/likes',
        headers={'api-key': 'test1'}
    )
    assert responce.status_code==201

    responce = client.delete(
        url=f'http://localhost:8000/api/tweets/{tweet_id}/likes',
        headers={'api-key': 'test1'}
    )
    assert responce.status_code == 200

    r = client.delete(
            f'http://localhost:8000/api/tweets/{tweet_id}',
                 headers={'api-key':'test1'})
    assert r.status_code==200
    #response = Response(r)
    #response.assert_status_code(200).validate(BaseGoodResponse)

def test_follow_user():
    r = client.post(
        url='http://localhost:8000/users/2/follow',
        headers = {'api-key': 'test1'}
    )
    assert r.status_code==200
    #Response(r).assert_status_code(200).validate(BaseGoodResponse)

def test_unfollow_user():
    r = client.delete(
        url='http://localhost:8000/users/2/follow',
        headers = {'api-key': 'test1'}
    )
    assert r.status_code==200
    #Response(r).assert_status_code(200).validate(BaseGoodResponse)