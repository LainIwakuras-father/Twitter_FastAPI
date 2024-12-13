import os
from typing import List

import aiofiles
from fastapi import UploadFile
from loguru import logger

from src.db.models.media import MediaOrm


async def save_upload_media(file: UploadFile):

    #upload_folder = "static"
    upload_folder = "src/static" #дл докер контейнера
    # Создаем директорию для картинки, если ее не
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    full_path = os.path.join(upload_folder, file.filename)
    # Сохраняем изображение
    async with aiofiles.open(full_path, mode="wb") as buffer:
        await buffer.write(file.file.read())
    logger.info(f"Uploaded file saved at {full_path}")

    return file.filename


async def delete_media(media: List[MediaOrm])->None:
    '''
    удаление из файловой системы
    '''
    for img in media:
        try:

            # Удаляем каждое изображение из файловой системы
            os.remove(os.path.join("static", str(img.file_path)))
            logger.debug(f"Изображение №{img.id} - {img.path_media} удалено")

        except FileNotFoundError:
            logger.error(f"Директория: {img.file_path} не найдена")

    logger.info("Все изображения удалены")

    # Проверка и очистка директории, если пустая

