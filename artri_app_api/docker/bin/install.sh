#!/bin/bash
set -ex

python manage.py collectstatic --noinput

python manage.py migrate
