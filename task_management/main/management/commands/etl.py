import os
import pandas as pd
from django.core.management.base import BaseCommand, CommandError
from main.models import Task

class Command(BaseCommand):
    help = 'Perform ETL operation'

    def handle(self, *args, **options):
        try:
            warehouse_folder = "../../../warehouse/files"
            os.makedirs(warehouse_folder, exist_ok=True)

            tasks_data = Task.objects.values()
            tasks_df = pd.DataFrame.from_records(tasks_data)

            tasks_file_path = os.path.join(warehouse_folder, "tasks.csv")
            tasks_df.to_csv(tasks_file_path, index=False)

            self.stdout.write(self.style.SUCCESS('ETL operation completed successfully'))

        except Exception as e:
            raise CommandError(f'An error occurred during the ETL operation: {str(e)}')