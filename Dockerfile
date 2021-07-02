FROM python:3.7-slim-buster

ENV PYTHONUNBUFFERED=1

ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_DEFAULT_REGION

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y

ENV AWS_ACCESS_KEY_ID $AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY $AWS_SECRET_ACCESS_KEY
ENV AWS_DEFAULT_REGION $AWS_DEFAULT_REGION

# Avoid cache purge by adding requirements first
ADD ./requirements.txt ./requirements.txt


RUN pip3 install -r ./requirements.txt

COPY . /app
WORKDIR /app

CMD [ "python", "manage.py", "runserver", "0.0.0.0:5000"]