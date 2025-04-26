import os

from celery import Celery
from kombu import Queue

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rabbit_sqs.settings')

app = Celery('rabbit_sqs', broker='amqp://guest:guest@localhost:5672/')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.task_default_queue = 'default'
app.conf.task_queues = {
    Queue('default', routing_key='default'),
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
