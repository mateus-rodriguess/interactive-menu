release: python manage.py migrate --noinput
web: gunicorn interactive_menu.wsgi --preload --log-file –
worker: celery --app interactive_menu.celery worker --loglevel=info