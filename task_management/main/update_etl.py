# update_etl.py
from celery import shared_task
from datetime import timedelta
import os
import django
import pandas as pd
from django.conf import settings
from .models import Task


def perform_etl(warehouse_folder):
    tasks_data = Task.objects.values()
    tasks_df = pd.DataFrame.from_records(tasks_data)
    tasks_file_path = os.path.join(warehouse_folder, "tasks.csv")
    tasks_df.to_csv(tasks_file_path, index=False)
    print(f"Data saved to CSV file: {tasks_file_path}")

@shared_task
def run_etl():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
    django.setup()
    
    warehouse_folder = "../warehouse/files"
    os.makedirs(warehouse_folder, exist_ok=True)
    
    # Call the ETL function
    perform_etl(warehouse_folder)

@shared_task
def periodic_run_etl():
    run_etl()
    print("ETL task executed at a periodic interval.")
