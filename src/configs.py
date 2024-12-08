# from pydantic_settings import BaseSettings
#
# class Settings(BaseSettings):
#     # Аннотация типов для проверки и валидации данных
#      MODE: str
#
#      DB_HOST: str
#      DB_PORT: int
#      DB_USER: str
#      DB_PASS: str
#      DB_NAME: str
#
#      @property
#      def DB_URL(self):
#         return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
#
#      # Подгружаем переменные окружения из файла
#      class Config:
#           env_file='.env'
#  # Сохраняем все в переменную для доступа в других файлах
# settings = Settings()

# old method!!!!!

import os

from dotenv import load_dotenv

load_dotenv()
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'

MODE = os.environ.get('MODE')


class Settings:
    DB_HOST = DB_HOST
    DB_PORT = DB_PORT
    DB_NAME = DB_NAME
    DB_USER = DB_USER
    DB_PASS = DB_PASS
    DB_URL = DB_URL
