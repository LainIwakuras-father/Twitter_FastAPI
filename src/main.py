import os

from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from src.api.v1.router import routers
from src.db.db import create_db
from src.utils.exception import custom_exception_handler, CustomException
from src.utils.get_current_user import get_current_user

#########################
# BLOCK WITH API ROUTES #
#########################
path = os.path.join(os.path.dirname(__file__), "static")
path_2 = os.path.join(os.path.dirname(__file__), "static/image")
app = FastAPI(title="Twitter",
              version="1.0.0",
              description="API для управления пользователями и твитами",
              debug=True,
              )

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
    StaticFiles(directory=path_2),
    name="image",
)
# dependencies=[Depends(get_current_user)]
app.add_exception_handler(CustomException, custom_exception_handler)






@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    await create_db()
    return HTMLResponse("index.html")






"""
классическая функция для запуска
"""
if __name__ == '__main__':
    #import asyncio
    import uvicorn

    #asyncio.run(create_db())
    uvicorn.run(app=app, host="127.0.0.1", port=8000)

