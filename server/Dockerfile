FROM python:3.12.2-alpine

RUN pip install Flask gunicorn --no-cache-dir

COPY src/ app/
WORKDIR /app

ENV PORT 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
