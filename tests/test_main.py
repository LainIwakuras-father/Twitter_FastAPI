from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app=app,base_url='http://localhost:8000')


def test_get_tweets(setup_and_teardown):
    response = client.get(
        'api/tweets',
        headers={'api-key':'test1'}
    )
    assert response.status_code==200


def test_get_user_for_id(setup_and_teardown):
    test_user, test_user2, test_user3= setup_and_teardown
    r = client.get(
        '/users/2',
        headers={'api-key': 'test1'}
        )
    assert r.status_code==200


def test_get_user_me_nonheaders(setup_and_teardown):
    r = client.get(
        url='/users/2',
        )
    assert r.status_code==401


def test_post_and_delete_tweet_and_like():
    r = client.post(
        json={"tweet_data": "This is a tweet to be deleted",'tweet_media_ids':[]},
        url='/api/tweets',
        headers={'api-key':'test1'})
    assert r.status_code==201

    tweet_id = r.json()["tweet_id"]

    responce = client.post(
        url=f'/api/tweets/{tweet_id}/likes',
        headers={'api-key': 'test1'}
    )
    assert responce.status_code==201

    responce = client.delete(
        url=f'/api/tweets/{tweet_id}/likes',
        headers={'api-key': 'test1'}
    )
    assert responce.status_code == 200

    r = client.delete(
            f'/api/tweets/{tweet_id}',
                 headers={'api-key':'test1'})
    assert r.status_code==200


def test_follow_user():
    r = client.post(
        url='/users/2/follow',
        headers = {'api-key': 'test1'}
    )
    assert r.status_code==200


def test_unfollow_user():
    r = client.delete(
        url='/users/2/follow',
        headers = {'api-key': 'test1'}
    )
    assert r.status_code==200
