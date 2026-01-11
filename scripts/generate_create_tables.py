import pandas as pd
import os

# 1️⃣ Get the folder of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2️⃣ Build path to raw CSVs relative to the script
csv_folder = os.path.join(script_dir, "..", "data", "raw")
csv_folder = os.path.normpath(csv_folder)  # normalizes slashes

# 3️⃣ Output SQL file in the sql folder
output_file = os.path.join(script_dir, "..", "sql", "create_tables.sql")
output_file = os.path.normpath(output_file)

# 4️⃣ List all CSV files in the folder
files = [f for f in os.listdir(csv_folder) if f.endswith(".csv")]

# 5️⃣ Generate CREATE TABLE statements
with open(output_file, "w", encoding="utf-8") as f:
    for file in files:
        table_name = os.path.splitext(file)[0]
        df = pd.read_csv(os.path.join(csv_folder, file))
        cols = df.columns.tolist()
        # Assumes first column is primary key (adjust if needed)
        sql_cols = ",\n    ".join([f"{col} TEXT" for col in cols])
        create_sql = f"CREATE TABLE {table_name} (\n    {sql_cols},\n    PRIMARY KEY({cols[0]})\n);\n\n"
        f.write(create_sql)

print(f"CREATE TABLE statements written to {output_file}")
print("Tables generated for:", [os.path.splitext(f)[0] for f in files])
