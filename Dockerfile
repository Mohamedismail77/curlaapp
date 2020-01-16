FROM ubuntu:16.04

RUN apt-get update -y

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirement.txt /app/requirements.txt

WORKDIR /app

COPY . /app

RUN bash curlLinks.sh

EXPOSE 5000

CMD ["bash","run.sh"]
