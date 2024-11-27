from fastapi import APIRouter

from backend.src.api.v1.endpoints.media import media_router
from backend.src.api.v1.endpoints.tweet import tweet_router
from backend.src.api.v1.endpoints.user import user_router

routers = APIRouter()

all_routers = [
 user_router,
 tweet_router,
 media_router
]

for router in all_routers:
     routers.include_router(router)
