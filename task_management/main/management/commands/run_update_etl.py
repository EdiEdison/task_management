from django.core.management.base import BaseCommand, CommandError
from main.update_etl import periodic_run_etl  

class Command(BaseCommand):
    help = 'Run periodic ETL operation'

    def handle(self, *args, **options):
        try:
            self.stdout.write(self.style.SUCCESS('Running periodic ETL operation...'))
            periodic_run_etl()
            self.stdout.write(self.style.SUCCESS('Periodic ETL operation completed successfully'))

        except Exception as e:
            raise CommandError(f'An error occurred during the periodic ETL operation: {str(e)}')
