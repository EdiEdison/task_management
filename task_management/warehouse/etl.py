import pandas as pd
import os
from main.models import Task

warehouse_folder = "./warehouse/files"

os.makedirs(warehouse_folder, exist_ok=True)

tasks_data = Task.objects.values()
tasks_df = pd.DataFrame.from_records(tasks_data)

tasks_file_path = os.path.join(warehouse_folder, "tasks.csv")
tasks_df.to_csv(tasks_file_path, index=False)



