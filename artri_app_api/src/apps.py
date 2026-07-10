from django.apps import AppConfig


class SrcConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src"
    # Mantém o app_label antigo para não precisar renomear tabelas/migrations
    # nem trocar AUTH_USER_MODEL.
    label = "authentication"

    def ready(self):
        from src.domains.accounts import signals  # noqa: F401
