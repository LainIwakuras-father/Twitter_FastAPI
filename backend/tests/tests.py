import pytest
from loguru import logger
from httpx import  AsyncClient

@pytest.mark.asyncio
async def test_get_user_id(client:AsyncClient):
    async with AsyncClient(
            transport=transport, app=app, base_url="http://localhost:8000/api"
    ) as ac:
        logger.debug("начало теста")
        response = await client.get("/users/2",headers='key_two')
        assert response.status_code == 200
        assert response.json()["result"] == True
        logger.info("тест завершился")



@pytest.mark.asyncio
async def test_delete_tweet(client:AsyncClient):
        logger.debug("начало теста")
        response = await client.post(
        "/tweets",
        json={"data": "This is a tweet to be deleted"},
        headers = 'key-one'
    )
        tweet_id = response.json()["id"]
        response =  await client.delete(f"/tweet/{tweet_id}",headers='key-one')
        assert response.status_code == 200
        assert response.json()["result"] == True
        logger.info("тест завершился")










