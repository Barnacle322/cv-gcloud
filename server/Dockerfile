FROM python:3.10.4-alpine

RUN pip install Flask==2.2.2 gunicorn --no-cache-dir

COPY src/ app/
WORKDIR /app

ENV PORT 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
