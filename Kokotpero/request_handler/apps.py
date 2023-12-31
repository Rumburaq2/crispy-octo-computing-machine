from django.apps import AppConfig


class RequestHandlerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'request_handler'

    def ready(self):
        import request_handler.signals