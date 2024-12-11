FROM python:3.11-slim
#ENV PYTHONDONTWRITEBYTECODE=1
#ENV PYTHONUNBUFFERED=1
LABEL "Creator"="Uriy Dolewsky"
WORKDIR /app
COPY re.txt .
RUN pip install --no-cache-dir --upgrade -r re.txt
COPY . .
#EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "127.0.0.1", "--port", "8000", "--reload"]