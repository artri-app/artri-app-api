#!/bin/bash
set -exu

NAME="artri_app_api.PE"                                             # Name of the application
SOCK_FILE=/var/run/artri_app_api.sock                                  # Sock file location with gunicorn process.
USER=root                                                     # the user to run as
GROUP=root                                                    # the group to run as
DJANGO_ASGI_MODULE="artri_app_api.asgi"                                # Django asgi

echo "Starting $NAME as $(whoami)"

## Activate the virtual environment

# Create the run directory if it doesn't exist
RUN_DIR=$(dirname $SOCK_FILE)
test -d "$RUN_DIR" || mkdir -p "$RUN_DIR"

exec gunicorn "${DJANGO_ASGI_MODULE}":application \
  --name $NAME \
  --worker-class=gevent \
  -k uvicorn.workers.UvicornWorker \
  --workers "$NUM_WORKERS" \
  --worker-connections "$WORKER_CONNECTIONS" \
  --timeout "$TIMEOUT" \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCK_FILE \
  --capture-output \
  --log-level=debug \
  --access-logfile='-' \
  --error-logfile='-'
