import pytest
from httpx import AsyncClient, ASGITransport
from loguru import logger

from main import app


@pytest.mark.asyncio
async def test_get_user_id(client: AsyncClient):
    ac: AsyncClient
    async with AsyncClient(
            transport=ASGITransport(app=app), app=app, base_url="http://localhost:8000/api"
    ) as ac:
        logger.debug("начало теста")
        response = await ac.get("/users/2", headers='key_two')
        assert response.status_code == 200
        assert response.json()["result"] == True
        logger.info("тест завершился")


@pytest.mark.asyncio
async def test_delete_tweet(client: AsyncClient):
    logger.debug("начало теста")
    response = await client.post(
        "/tweets",
        json={"data": "This is a tweet to be deleted"},
        headers='key-one'
    )
    tweet_id = response.json()["id"]
    response = await client.delete(f"/tweet/{tweet_id}", headers='key-one')
    assert response.status_code == 200
    assert response.json()["result"] == True
    logger.info("тест завершился")
