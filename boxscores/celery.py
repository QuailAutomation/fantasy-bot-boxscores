import os

from celery import Celery

CELERY_IMPORTS = ("tasks", )
CELERY_RESULT_BACKEND=os.getenv("CELERY_RESULT_BACKEND", 'redis://localhost')
BROKER_URL=os.getenv("BROKER_URL", 'amqp://localhost:5672//')

CELERY_TASK_RESULT_EXPIRES = 300

cel = Celery('boxscores, backend=CELERY_RESULT_BACKEND, include=['boxscores.worker'])
