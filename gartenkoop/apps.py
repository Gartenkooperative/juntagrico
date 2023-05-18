from django.apps import AppConfig


class GartenkoopConfig(AppConfig):
    name = 'gartenkoop'
    verbose_name = "gartenkooperative"

    def ready(self):
        from . import signals  # noqa: F401
