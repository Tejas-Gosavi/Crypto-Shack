import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('crypto')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_coins_data_15s': {
        'task': 'coins.tasks.get_coins_data',
        'schedule': 15.0
    },
}

app.autodiscover_tasks()


# celery -A crypto worker -l INFO
# celery -A crypto beat -l INFO 
# redis-server