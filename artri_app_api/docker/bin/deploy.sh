export DJANGO_SETTINGS_MODULE="artri_app_api.settings" # Django settings for environment

bash ./docker/bin/install.sh
if [ "$ENV" = "production" ]; then
  bash ./docker/bin/uvicorn_start.sh
else
  bash ./docker/bin/runserver_start.sh
fi
