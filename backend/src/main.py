from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError

from backend.src.utils.exception.exception import custom_http_exception_handler, custom_requestvalueError_handler
from routing.router import all_routers

app = FastAPI()


app.add_exception_handler(HTTPException,custom_http_exception_handler)
app.add_exception_handler(RequestValidationError,custom_requestvalueError_handler)

for router in all_routers:
    app.include_router(router)

"""
классическая функция для запуска
"""
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app, host="127.0.0.1", port=8000)

