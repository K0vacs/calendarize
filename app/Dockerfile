# This is a Docker configuration file that is called by the Docker Compose web Image

FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
COPY requirements.txt /src/
RUN pip install -r requirements.txt
COPY . /src/