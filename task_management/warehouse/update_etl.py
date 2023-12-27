# update_etl.py
from celery import Celery
from celery.decorators import periodic_task
from datetime import timedelta
import os
import pandas as pd
from django.core.management import setup_environ
from django.conf import settings
from main.models import Task

app = Celery('update_etl', broker='pyamqp://guest:guest@localhost//')

def perform_etl(warehouse_folder):
    tasks_data = Task.objects.values()
    tasks_df = pd.DataFrame.from_records(tasks_data)
    tasks_file_path = os.path.join(warehouse_folder, "tasks.csv")
    tasks_df.to_csv(tasks_file_path, index=False)
    print(f"Data saved to CSV file: {tasks_file_path}")

@app.task
def run_etl():
    setup_environ(settings)
    
    warehouse_folder = "./warehouse/files"
    os.makedirs(warehouse_folder, exist_ok=True)
    
    # Call the ETL function
    perform_etl(warehouse_folder)

@periodic_task(run_every=timedelta(hours=1), name="run_etl_periodically")
def periodic_run_etl():
    run_etl()
    print("ETL task executed at a periodic interval.")
