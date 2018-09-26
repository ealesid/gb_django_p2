from django.apps import AppConfig


class AppaccountsConfig(AppConfig):
    name = 'appAccounts'

    def ready(self):
        import appAccounts.signals
