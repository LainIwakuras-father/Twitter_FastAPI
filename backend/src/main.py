from fastapi import FastAPI

from backend.src.utils.exception import custom_exception_handler, CustomException
from routing.router import all_routers

app = FastAPI(title="Twitter", debug=True)

for router in all_routers:
    app.include_router(router)


app.add_exception_handler(CustomException,custom_exception_handler)
"""
классическая функция для запуска
"""
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app, host="127.0.0.1", port=8000)

