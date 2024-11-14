from fastapi import FastAPI
from routing.router import all_routers

app = FastAPI(title="Twitter", debug=True)

for router in all_routers:
    app.include_router(router)

"""
классическая функция для запуска
"""
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app, host="127.0.0.1", port=8000)

