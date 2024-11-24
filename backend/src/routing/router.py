from backend.src.routing.media import media_router
from backend.src.routing.tweet import tweet_router
from backend.src.routing.user import user_router
from backend.src.routing.work_db import db_router

all_routers = [
 user_router,
 db_router,
 tweet_router,
 media_router
]


