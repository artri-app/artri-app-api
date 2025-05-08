# DOCKER IMAGE
# Official Python 3.12 image based on buster Debian
FROM python:3.12-slim
ARG DEBIAN_FRONTEND=noninteractive
ARG ENV
ENV ENV=$ENV

# set work directory
WORKDIR /opt/artriapp

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install os dependencies
RUN apt-get update \
    && apt-get --no-install-recommends install -y curl gettext \
    gcc libldap2-dev libsasl2-dev slapd ldap-utils libldap-common \
    libmagic1 libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0 libffi-dev libjpeg-dev libopenjp2-7-dev \
    && apt-get clean

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.pip ./requirements.pip
RUN pip install -r ./requirements.pip

# copy project
COPY docker/bin/ ./docker/bin/
COPY docker/django/ ./docker/django/
COPY artri_app_api/ ./artri_app_api/
COPY manage.py .

RUN chmod +x ./docker/bin/*.sh
