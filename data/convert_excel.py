import pandas as pd
from pathlib import Path

# Get absolute path of this file's folder
BASE_DIR = Path(__file__).resolve().parent

# Paths
excel_path = BASE_DIR / "Gen_AI Dataset.xlsx"
csv_path = BASE_DIR / "shl_catalog.csv"

# Read Excel and save CSV
df = pd.read_excel(excel_path)
df.to_csv(csv_path, index=False)

print("CSV file created successfully at:", csv_path)
