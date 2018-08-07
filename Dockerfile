FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /django-project
WORKDIR /django-project
ADD requirements.txt /django-project/
RUN pip install -r requirements.txt
ADD . /django-project/
RUN apt-get update && apt-get -y install postgresql
