from django.apps.config import AppConfig


class ASDAMainConfig(AppConfig):
    name = 'ASDA'
    verbose_name = 'ASDA main' # this name will display in the Admin. You may translate this value if you want using ugettex_lazy

    def ready(self):
        import ASDA.signals.handlers
