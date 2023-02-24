FROM python:3.9-alpine

COPY . .
RUN apt-get install build-essentials gcc && \
    pip install -r requirements.txt --no-cache-dir