# syntax=docker/dockerfile:1.2

#-----------------------------------------------------------------------------

##### Production Image
FROM dockerhub7788/add_oracle
LABEL maintainer kepler777888@gmail.com

ARG PROJECT_NAME=checkin_system_web
ARG PROJECT_PATH=.
ARG ENV=.env

RUN echo "deb http://opensource.nchc.org.tw/debian/ stretch main" >/etc/apt/sources.list \
    && echo "deb http://opensource.nchc.org.tw/debian/ stretch-updates main" >>/etc/apt/sources.list

### Copy the Project
COPY ${PROJECT_PATH}/${PROJECT_NAME} /${PROJECT_NAME}
COPY ${PROJECT_PATH}/requirements.txt /${PROJECT_NAME}
COPY ./${ENV} /${PROJECT_NAME}/.env

WORKDIR /${PROJECT_NAME}

### Install all python dependency libs
RUN pip install --no-index --find-links=/tmp/wheels uwsgi
RUN pip install --no-index --find-links=/tmp/wheels django-auth-ldap
RUN pip install -r ./requirements.txt

### COPY the uwsgi configuration file 
COPY ${PROJECT_PATH}/${PROJECT_NAME}/uwsgi.ini /etc/uwsgi/uwsgi.ini


RUN mkdir -p  /log \
    && chown -R www-data:www-data /log

### Start uWSGI on container startup
CMD ["/usr/local/bin/uwsgi", "--ini", "/etc/uwsgi/uwsgi.ini"]
