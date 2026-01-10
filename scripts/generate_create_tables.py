import pandas as pd
import os

csv_folder = "../data/raw"  # relative path from scripts folder
output_file = "../sql/create_tables_auto.sql"

files = [f for f in os.listdir(csv_folder) if f.endswith(".csv")]

with open(output_file, "w") as f:
    for file in files:
        table_name = os.path.splitext(file)[0]
        df = pd.read_csv(os.path.join(csv_folder, file))
        cols = df.columns.tolist()
        sql_cols = ",\n    ".join([f"{col} TEXT" for col in cols])
        create_sql = f"CREATE TABLE {table_name} (\n    {sql_cols},\n    PRIMARY KEY({cols[0]})\n);\n\n"
        f.write(create_sql)

print(f"CREATE TABLE statements written to {output_file}")
