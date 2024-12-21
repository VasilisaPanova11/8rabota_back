FROM python:3.11.5


RUN apt-get update \
    && apt-get install -y libmariadb-dev \
    python3-pip build-essential \
    libcurl4-openssl-dev libssl-dev \
    && pip install --upgrade pip

RUN pip install --upgrade pip

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
