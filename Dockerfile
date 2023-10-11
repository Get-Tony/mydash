FROM python:3.11.6-slim-bookworm

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/ .

EXPOSE 8501
