# from backend.src.routing.follow import follow_router
# from backend.src.routing.images import image_router
# from backend.src.routing.likes import likes_router
# from backend.src.routing.tweet import tweet_router
from backend.src.routing.user import user_router
from backend.src.routing.work_db import db_router

all_routers = [
 user_router,
 db_router
]

 # follow_router,
 # likes_router,
 # image_router,
 # tweet_router