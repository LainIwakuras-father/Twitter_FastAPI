FROM python:3.11


COPY requirements.txt /

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src /src

# gunicorn
# CMD gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
CMD ["uvicorn", "src.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]