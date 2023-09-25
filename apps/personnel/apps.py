from django.apps import AppConfig


class PersonnelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.personnel'


class CoreConfig(AppConfig):
    name = 'apps.personnel'
