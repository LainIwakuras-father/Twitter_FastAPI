#ПИШИ СВОЮ ВЕРСИЮ ПИТОНА
FROM python:3.12.0-slim

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

LABEL "Creator"="Uriy Dolewsky"

WORKDIR /app

COPY requirements-base.txt /app/requirements-base.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements-base.txt

COPY src /app/src

#CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]