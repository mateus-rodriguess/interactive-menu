import time
from datetime import datetime
from interactive_menu.celery import app
from celery import shared_task
from celery.schedules import crontab
from .models import  Config

app.conf.beat_schedule =  {
    'create-task': {
        'task': 'apps.core.tasks.create_task',
        'schedule': crontab(minute = "*"),
        #'args': ("16"),
    },
}

@app.task
def create_task():
    print('\x1b[6;30;42m' + ">>>>>>>> Cron celery test " + str(datetime.now()) + " <<<<<<<<<<<<<<" + '\x1b[0m')

@shared_task
def add(x, y):
    return x + y
