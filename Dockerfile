FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /django_app
WORKDIR /django_app
ADD requirements.txt /django_app/
RUN pip install -r requirements.txt
ADD . /django_app/
RUN apt-get update && apt-get -y install postgresql
