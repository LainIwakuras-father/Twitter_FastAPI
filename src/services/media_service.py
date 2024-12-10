from fastapi import UploadFile
from loguru import logger

from src.utils.media_work_file import save_upload_media
from src.utils.unitofwork import AbstractUnitOfWork


class MediaService:
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow

    async def add_media(self, file: UploadFile) -> int:
        path = await save_upload_media(file)  # Сохранение изображения в файловой системе
        logger.debug(f"Загрузка изображение {file}")
        async with self.uow:
            data = dict(file_path=path)
            media_id = await self.uow.media.add_one(data)
            await self.uow.commit()
            return media_id

    async def delete_media(self):
        pass
