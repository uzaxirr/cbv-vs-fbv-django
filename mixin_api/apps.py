from django.apps import AppConfig


class MixinApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mixin_api'
