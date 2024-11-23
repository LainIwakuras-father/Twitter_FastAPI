from fastapi import FastAPI

from backend.src.routing.router import all_routers
from backend.src.utils.exception import custom_exception_handler, CustomException

#########################
# BLOCK WITH API ROUTES #
#########################
app = FastAPI(title="Twitter",
              version="1.0.0",
              description="API для управления пользователями и твитами",
              debug=True)

for router in all_routers:
    app.include_router(router)

app_api = FastAPI()

for router in all_routers:
    app_api.include_router(router)

app.mount("/api", app_api)


app.add_exception_handler(CustomException,custom_exception_handler)
"""
классическая функция для запуска
"""
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app, host="127.0.0.1", port=8000)

