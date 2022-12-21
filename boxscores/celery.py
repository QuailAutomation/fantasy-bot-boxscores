from celery import Celery

CELERY_IMPORTS = ("tasks", )
CELERY_RESULT_BACKEND = "redis://localhost"
BROKER_URL = "amqp://localhost:5672//"
CELERY_TASK_RESULT_EXPIRES = 300

cel = Celery('boxscores', backend="redis://localhost", include=['boxscores.worker'])
