FROM python:3.11-slim

WORKDIR /app
COPY . ./
RUN pip install -r requirements.txt


CMD ["gunicorn", "main:app", "-k", "uvicorn.workers.UvicornWorker", "-c", "gunicorn_settings.py"]

EXPOSE 8000