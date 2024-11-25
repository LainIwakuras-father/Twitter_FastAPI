import os
import aiofiles
from loguru import logger
from fastapi import UploadFile



async def save_upload_media(file: UploadFile):
    upload_folder = "static"
    # Создаем директорию для картинки, если ее не
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    full_path =os.path.join(upload_folder,file.filename)
    # Сохраняем изображение
    async with aiofiles.open(full_path,mode="wb") as buffer:
        await buffer.write(file.file.read())
    logger.info(f"Uploaded file saved at {full_path}")

    return file.filename