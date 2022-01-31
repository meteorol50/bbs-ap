FROM python:3.8

WORKDIR /app

ENV PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.8/site-packages/

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . .
