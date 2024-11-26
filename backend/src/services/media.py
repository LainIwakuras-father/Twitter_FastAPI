from typing import List


from loguru import logger
from fastapi import UploadFile
from sqlalchemy import update

from backend.src.db import async_session
from backend.src.models.media import MediaOrm
from backend.src.utils.media import save_upload_media


class MediaService:
     @classmethod
     async def add_media(cls,file: UploadFile)->MediaOrm|None:
          path = await save_upload_media(file)# Сохранение изображения в файловой системе
          logger.debug(f"Загрузка изображение {file}")
          async  with async_session() as db:
                 media = MediaOrm( file_path=path)  # Создание экземпляра изображения
                 db.add(media)# Добавление изображения в БД
                 await db.commit()# Сохранение в БД
                 await db.refresh(media)
                 return media

     @classmethod
     async def update_media(cls,tweet_media_ids:List[int],tweet_id:int)->None:
         '''
         Привязка загруженных изоброжений к твиту
         '''
         logger.debug(
             f"Обновление изображений по id: {tweet_media_ids}, tweet_id: {tweet_id}"
         )
         async  with (async_session() as db):
             for media_id in tweet_media_ids:
                 query = (update(MediaOrm)
                          .where(MediaOrm.id==media_id)
                          .values(tweet_id=tweet_id))
                 await db.execute(query)
                 await db.flush()

             await db.commit()


     @classmethod
     async def delete_media(cls):
         '''
         сделать так что бы когда удалялся твит удалялось и фото из БД и файловой системы
         '''
         pass






