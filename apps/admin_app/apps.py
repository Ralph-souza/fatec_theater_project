from django.apps import AppConfig


class AdminAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.admin_app'


class CoreConfig(AppConfig):
    name = 'apps.admin_app'
