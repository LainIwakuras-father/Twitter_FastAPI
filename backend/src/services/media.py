from loguru import logger

from backend.src.db.db import async_session
from backend.src.models.media import MediaOrm
from backend.src.utils.media import save_upload_media


class MediaService:
     @classmethod
     async def upload_media(cls,tweet_id:int,file_path:str)->int:
          path = await save_upload_media(file_path)# Сохранение изображения в файловой системе
          logger.debug(f"Загрузка изображение {file_path}")
          async  with async_session() as db:
                 media = MediaOrm(tweet_id=tweet_id, file_path=path)  # Создание экземпляра изображения
                 db.add(media)# Добавление изображения в БД
                 db.commit()# Сохранение в БД
                 return media.id




