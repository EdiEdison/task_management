import os
import pandas as pd
from django.core.management import setup_environ
from django.conf import settings
import time
from main.models import Task, Project

def perform_etl(warehouse_folder):
    tasks_data = Task.objects.values()
    projects_data = Project.objects.values()

    tasks_df = pd.DataFrame.from_records(tasks_data)
    projects_df = pd.DataFrame.from_records(projects_data)

    tasks_file_path = os.path.join(warehouse_folder, "tasks.csv")
    projects_file_path = os.path.join(warehouse_folder, "projects.csv")

    tasks_df.to_csv(tasks_file_path, index=False)
    projects_df.to_csv(projects_file_path, index=False)

    print(f"Data saved to CSV files: {tasks_file_path}, {projects_file_path}")

if __name__ == "__main__":
    setup_environ(settings)
    warehouse_folder = "./warehouse/files"
    os.makedirs(warehouse_folder, exist_ok=True)

    while True:
        perform_etl(warehouse_folder)
        time.sleep(3600)  
