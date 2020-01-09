from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # Implementing signal in way presented by django documentation: https://docs.djangoproject.com/en/3.0/ref/signals/#post-migrate
    def ready(self):
        import users.signals
