# django compilestatic stage
FROM python:3.12-slim AS django-static-stage
ARG ENV

# set work directory
WORKDIR /opt/artri-app-api

# install dependencies
RUN apt-get update \
    && apt-get --no-install-recommends install -y gcc libldap2-dev libsasl2-dev slapd ldap-utils libldap-common libmagic1 \
    && apt-get clean
RUN pip install --upgrade pip
COPY ./requirements.pip ./requirements.pip
RUN pip install -r ./requirements.pip
# copy project
COPY ./artri_app_api/artri_app_api/ ./artri_app_api/
COPY ./artri_app_api/manage.py ./

# run django collectstatic
RUN python manage.py collectstatic --noinput --settings=artriapp.settings."$ENV"

# production stage
FROM nginx:stable AS production-stage

# Copy nginx config files
COPY ./artri_app_api/docker/nginx/default.conf /etc/nginx/conf.d/default.conf

# Get front static files

# Get django static files
RUN mkdir -p /opt/artri-app-api/artri_app_api/staticfiles/
COPY --from=django-static-stage /opt/artri-app-api/artri_app_api/staticfiles/ /opt/artri-app-api/artri_app_api/staticfiles/
