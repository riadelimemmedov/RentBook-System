from .celery import app as celery_app

__all__ = ['celery_app']#We need to make this celery instance available throughout out project
