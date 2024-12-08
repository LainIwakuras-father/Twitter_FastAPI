from loguru import logger

from db.db import create_database


async def create_tables():
    try:
        await create_database()
        logger.info("message: Models created!")
    except:
        logger.error("server error")
