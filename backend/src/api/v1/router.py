from backend.src.api.v1.endpoints.media import media_router
from backend.src.api.v1.endpoints.tweet import tweet_router
from backend.src.api.v1.endpoints.user import user_router
from backend.src.api.v1.endpoints.work_db import db_router

all_routers = [
 user_router,
 db_router,
 tweet_router,
 media_router
]


