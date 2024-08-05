"""
Django command to wait for db to be available
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError #error that pycopg2 throws when db not reeady

from django.db.utils import OperationalError #error that django throws when db not reeady
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self, *args, **options):
        """Entry point for command"""
        self.stdout.write('Waiting for DB...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default']) #will check and will throw exception if DB not yes available
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('DB unavailable, waiting 1s')
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('Database available!'))

