from fastapi import APIRouter

from src.api.endpoints.media import media_router
from src.api.endpoints.tweet import tweet_router
from src.api.endpoints.user import user_router

routers = APIRouter()

all_routers = [
    user_router,
    tweet_router,
    media_router
]

for router in all_routers:
    routers.include_router(router)
