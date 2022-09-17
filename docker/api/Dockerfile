FROM python:3.8.2

RUN pip install --upgrade pip

WORKDIR /src/api

COPY ./api /src/api
ADD .env /src

RUN pip install -r requirements.txt