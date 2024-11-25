from typing import List


from loguru import logger
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from backend.src.db.db import async_session
from backend.src.models.likes import LikeOrm
from backend.src.models.tweet import TweetOrm

from backend.src.schemas.tweet_schema import TweetWrite, TweetRead
from backend.src.services.media import MediaService
from backend.src.utils.exception import CustomException


class TweetService:

    @classmethod
    async def add_tweet(cls,tweet:TweetWrite):
        logger.debug('Добавление твита')
        async  with async_session() as db:
            new_tweet = TweetOrm(
                data=tweet.data, author_id=tweet.author_id
            )
            # Добавляем в индекс, фиксируем, но не записываем в БД!!!
            db.add(new_tweet)
            await db.commit()
            await db.refresh(new_tweet)


            tweet_media_ids = tweet.tweet_media_ids
            if tweet_media_ids and tweet_media_ids != []:
                # Привязываем изображения к твиту
                  await MediaService.update_media(tweet_media_ids=tweet_media_ids,tweet_id=new_tweet.id)


            # Сохраняем в БД все изменения (новый твит + привязку картинок к твиту)

            return new_tweet.id

    @classmethod
    async def get_tweets(cls)->List[TweetRead]:
        logger.debug('просмотр ленты твитов')
        async  with async_session() as db:
            query = (select(TweetOrm)
                    .options(
                     joinedload(TweetOrm.author),
                     joinedload(TweetOrm.likes).subqueryload(LikeOrm.user),
                     joinedload(TweetOrm.media))
                     .order_by(TweetOrm.created_at.desc())
                     )

            result =  await db.execute(query)
            return result.unique().scalars().all()



    @classmethod
    async def get_tweet(cls,tweet_id) -> List[TweetRead]:
            logger.debug(f"Поиск твита по id: {tweet_id}")
            async  with async_session() as db:
                query = select(TweetOrm).where(TweetOrm.id == tweet_id)
                tweet = await db.execute(query)

                return tweet.scalar_one_or_none()

    @classmethod
    async def delete_tweet(cls, id: int):
        logger.debug('удаление твита')
        async  with async_session() as db:
            existing_tweet = await db.get(TweetOrm, id)
            if existing_tweet is None:
                logger.error("Твит не найден")
                raise CustomException(status_code=404, detail="not found")

            await db.delete(existing_tweet)
            await db.commit()