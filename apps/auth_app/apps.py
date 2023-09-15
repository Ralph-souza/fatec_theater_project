from django.apps import AppConfig


class AuthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.auth_app'


class CoreConfig(AppConfig):
    name = 'apps.auth_app'
