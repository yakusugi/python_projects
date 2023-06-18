import pandas as pd
import sys

if len(sys.argv) < 2:
    print("Please specify the excel file as an argument")
    sys.exit(1)

try:
    df = pd.read_excel(sys.argv[1], engine='openpyxl')
    print(df)
except FileNotFoundError:
    print(f"Error: The file {sys.argv[1]} could not be found.")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    sys.exit(1)


