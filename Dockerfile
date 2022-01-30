FROM python:3.8

WORKDIR /app

RUN pip install fastapi uvicorn pydantic[email] 'SQLAlchemy<1.4' aiomysql
COPY . .
