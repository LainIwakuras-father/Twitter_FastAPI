from fastapi import APIRouter

image_router = APIRouter(tags=["image"])


@image_router.post('/api/medias')
async def add_picture():
    pass