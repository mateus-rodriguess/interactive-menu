release: python manage.py sync_roles & python manage.py migrate --noinput
worker: celery --app pythonpro.celery worker --loglevel=info