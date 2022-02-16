release: python manage.py collectstatic --noinput

web: gunicorn interactive_menu.wsgi:application --log-file - --log-level debug

