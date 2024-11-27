from fastapi import FastAPI,Depends,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from backend.src.api.v1.router import  routers
from backend.src.utils.exception import custom_exception_handler, CustomException
from backend.src.utils.get_current_user import get_current_user
#########################
# BLOCK WITH API ROUTES #
#########################
app = FastAPI(title="Twitter",
              version="1.0.0",
              description="API для управления пользователями и твитами",
              debug=True,
              )

app.mount("/src/static", StaticFiles(directory="/static"), name="static")


app.include_router(routers,dependencies=[Depends(get_current_user)])
app.add_exception_handler(CustomException,custom_exception_handler)


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return HTMLResponse("Hello World!")
"""
классическая функция для запуска
"""
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app, host="127.0.0.1", port=8000)

