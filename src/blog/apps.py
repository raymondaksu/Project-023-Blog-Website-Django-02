from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self) -> None:
        import blog.signals
