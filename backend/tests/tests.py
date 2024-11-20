import pytest


@pytest.mark.user
class TestUser:
    async def test_get_user_id(self):
        pass

@pytest.mark.tweets
class TestTweets:
    async def test_create_tweet(self):
        pass
    async def test_delete_tweet(self):
        pass
    async def test_get_tweets(self):
        pass


@pytest.mark.follow
class TestFollow:
    async def test_add_follow(self):
        pass
    async def test_delete_follow(self):
        pass

@pytest.mark.likes
class TestLike:
    async  def test_add_like(self):
        pass
    async def test_delete_like(self):
        pass









