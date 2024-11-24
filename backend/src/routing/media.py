from loguru import logger
from fastapi import APIRouter, UploadFile

from backend.src.schemas.tweet_schema import MediaOut
from backend.src.services.media import MediaService
from backend.src.utils.exception import CustomException

media_router = APIRouter(prefix='/api/medias',tags=["image"])



@media_router.post('',status_code=201)
async def add_picture(tweet_id:int,file: UploadFile):
    """
       Загрузка изображения к твиту
    """
    if not file:
        logger.error("Изображение не передано в запросе")
        raise CustomException(
            status_code=400,
            detail="The image was not attached to the request")

    media_id = await MediaService.upload_media(tweet_id=tweet_id,file_path=file)
    return {'media_id':media_id}