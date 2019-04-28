FROM bitnami/python:3.6.8-debian-9-r73-prod

LABEL maintainer "apgpavel@gmail.com"

ARG TM_VERSION=0.1

RUN mkdir -p /app
COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
RUN chmod -R 444 /app

CMD [ "python", "./init.py" ]

