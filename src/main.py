import os

from loguru import logger
from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.api.v1.router import routers
from src.db.db import create_db, async_session, drop_db
from src.db.models.user import UserOrm
from src.utils.exception import custom_exception_handler, CustomException
from src.utils.get_current_user import get_current_user

#########################
# BLOCK WITH API ROUTES #
#########################
"""СОЗдание пользователя в БД"""
async def create_test_user(db:AsyncSession, name: str, api_key:str):
        query = select(UserOrm).filter(UserOrm.name == name)
        res = await db.execute(query)
        user = res.scalar_one_or_none()

        if user:
            return user

        user = UserOrm(name=name, api_key=api_key)
        db.add(user)
        await db.commit()
        await db.refresh(user)
        await db.close()
        return user



path = os.path.join(os.path.dirname(__file__), "static")

app = FastAPI(title="Twitter",
              version="1.0.0",
              description="API для управления пользователями и твитами",
              debug=True,

              )
#lifispan=lifispan
app_api = FastAPI()

app_api.include_router(routers)
app.include_router(routers, dependencies=[Depends(get_current_user)])
app.mount("/api", app_api)
app.mount(
    "/",
    StaticFiles(directory=path, html=True),
    name="static",
)
app.mount(
    "/static",
    StaticFiles(directory=path),
    name="image",
)
# dependencies=[Depends(get_current_user)]
app.add_exception_handler(CustomException, custom_exception_handler)

db:AsyncSession = async_session()
@app.on_event("startup")
async def startup_events():
         await create_db()
         logger.debug('DB CREATED')
         await create_test_user(db=db, name="test1", api_key="test")
         await create_test_user(db=db, name="test2", api_key="key_test2")
         logger.debug('test users CREATED')




@app.on_event("shutdown")
async def shutdown_event():
    await db.close()
    #await drop_db()
    #logger.debug('DB DROP')


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return HTMLResponse("index.html")


"""
классическая функция для запуска
"""
if __name__ == '__main__':
    #import asyncio
    import uvicorn

    #asyncio.run(create_db())
    uvicorn.run(app=app, host="127.0.0.1", port=8000)

