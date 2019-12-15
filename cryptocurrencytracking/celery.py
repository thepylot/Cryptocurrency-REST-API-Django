import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptocurrencytracking.settings')

app = Celery('cryptocurrencytracking')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()