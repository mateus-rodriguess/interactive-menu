import time
from datetime import datetime
from interactive_menu.celery import app
from celery import shared_task
from celery.schedules import crontab
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)

app.conf.beat_schedule =  {
    'create-task': {
        'task': 'apps.core.tasks.create_task',
        'schedule': crontab(minute = "59"),
        #'args': ("16"),
    },
}

@app.task
def create_task():
    logger.info("The sample task just ran.")

@shared_task
def add(x, y):
    return x + y
