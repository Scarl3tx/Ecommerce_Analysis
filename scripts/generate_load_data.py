import os
import pandas as pd

# 1️⃣ Get path of current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2️⃣ Paths to CSV folder and output SQL
csv_folder = os.path.join(script_dir, "..", "data", "raw")
csv_folder = os.path.normpath(csv_folder)

output_file = os.path.join(script_dir, "..", "sql", "load_data.sql")
output_file = os.path.normpath(output_file)

# 3️⃣ List all CSVs
csv_files = [f for f in os.listdir(csv_folder) if f.endswith(".csv")]

# 4️⃣ Generate .import statements
with open(output_file, "w", encoding="utf-8") as f:
    f.write("-- SQLite CSV import script\n")
    f.write(".mode csv\n\n")
    for csv_file in csv_files:
        table_name = os.path.splitext(csv_file)[0]  # file name without extension
        csv_path = os.path.join("..", "data", "raw", csv_file).replace("\\", "/")  # SQLite likes forward slashes
        f.write(f".import '{csv_path}' {table_name}\n")

print(f"load_data_auto.sql created with {len(csv_files)} tables.")
