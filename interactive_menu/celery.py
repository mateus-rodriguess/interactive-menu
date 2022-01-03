import os
from django.conf import settings
from celery import Celery
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'interactive_menu.settings')
 
app = Celery('interactive_menu')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
