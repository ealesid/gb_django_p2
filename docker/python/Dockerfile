FROM python:3.6.6

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y cron vim rsyslog gcc libc-dev unixodbc-dev apt-transport-https \
    && apt-get autoremove && apt-get autoclean
RUN echo "Europe/Moscow" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata

# Project Files and Settings
ARG PROJECT=.
ARG PROJECT_DIR=/srv/web/${PROJECT}
RUN mkdir -p $PROJECT_DIR

WORKDIR $PROJECT_DIR
RUN pwd && ls -la
COPY requirements.txt $PROJECT_DIR
RUN pip install -r requirements.txt
#ADD . $PROJECT_DIR
