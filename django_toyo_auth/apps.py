from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_toyo_auth'

    def ready(self):
        from . import signals
