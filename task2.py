import pandas as pd

file_path = "Crypto_Analytics_Project(1).xlsm"

df = pd.read_excel(
    file_path,
    sheet_name="Raw Data"
)

required_columns = [
    "Coin Name",
    "Symbol",
    "Price (USD)",
    "Volume (24h) USD",
    "Market Cap",
    "Circulating Supply"
]

task2_df = df[required_columns].copy()

task2_df.to_excel(
    "Task2_Python_Output.xlsx",
    index=False
)

print("Task 2 Python completed!")
print(f"Rows exported: {len(task2_df)}")
print(task2_df.head())