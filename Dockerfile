FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN apt-get update
RUN apt-get install -y --no-install-recommends gcc libc-dev python3-dev default-libmysqlclient-dev

RUN pip install -r /requirements.txt

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN useradd user
USER user

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000