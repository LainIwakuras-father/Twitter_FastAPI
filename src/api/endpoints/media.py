from fastapi import APIRouter, UploadFile
from loguru import logger

from src.api.schemas.tweet_schema import MediaOut
from src.api.dependencies import media_service
from src.utils.exception import CustomException

media_router = APIRouter(prefix='/api/medias', tags=["image"])


@media_router.post(
    '',
    response_model=MediaOut,
    status_code=201)
async def add_picture(
        file: UploadFile,
        service: media_service
):
    """
       Загрузка изображения к твиту
    """
    if not file:
        logger.error("Изображение не передано в запросе")
        raise CustomException(
            status_code=400,
            detail="The image was not attached to the request")

    media_id = await service.add_media(file=file)
    return {'media_id': media_id}
