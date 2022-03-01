import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand
 
class Command(BaseCommand):
    """Django command to pause execution until db is available"""
 
    def handle(self, *args, **options):
        self.stdout.write('_______________ DJANGO __________________')
        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waititng 3 second...')
                self.stdout.write('_______________ DJANGO __________________')
                time.sleep(3)
 
        self.stdout.write(self.style.SUCCESS('Database available!'))
       