from typing import List

from loguru import logger
from sqlalchemy import update

from src.db.models.media import MediaOrm
from src.repositories.base_repository import SQLAlchemyRepository


class MediaRepository(SQLAlchemyRepository):
    model = MediaOrm

    async def update_info(self, tweet_media_ids: List[int], tweet_id: int):
        '''
        Привязка загруженных изоброжений к твиту
        '''
        logger.debug(
            f"Обновление изображений по id: {tweet_media_ids}, tweet_id: {tweet_id}"
        )
        for media_id in tweet_media_ids:
            query = (update(self.model)
                     .where(self.model.id == media_id)
                     .values(tweet_id=tweet_id))
            await self.session.execute(query)
            await self.session.flush()


'''
сделать так что бы когда удалялся твит удалялось и фото из БД и файловой системы
'''
