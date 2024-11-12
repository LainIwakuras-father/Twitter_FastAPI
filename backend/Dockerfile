FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt

RUN pip install --no-cache-dir -r requirements

COPY . .

CMD["uvicorn","app.main:app","--host","--port","8080"]
