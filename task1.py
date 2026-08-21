import pandas as pd
import re

file_path = "Crypto_Analytics_Project(1).xlsm"

df = pd.read_excel(
    file_path,
    sheet_name="Raw Data"
)

print("Raw Data loaded:", len(df), "rows")

df["First Letter"] = (
    df["Coin Name"]
    .astype(str)
    .str.strip()
    .str[0]
    .str.upper()
)

allowed_letters = list("AEIOUBCD")

filtered_df = df[
    df["First Letter"].isin(allowed_letters)
].copy()

def clean_volume(value):
    value = str(value).replace("$", "").replace(",", "").strip()

    multiplier = 1

    if value.upper().endswith("B"):
        multiplier = 1_000_000_000
        value = value[:-1]
    elif value.upper().endswith("M"):
        multiplier = 1_000_000
        value = value[:-1]
    elif value.upper().endswith("K"):
        multiplier = 1_000
        value = value[:-1]

    try:
        return float(value) * multiplier
    except:
        return 0

filtered_df["Volume Numeric"] = (
    filtered_df["Volume (24h) USD"].apply(clean_volume)
)

filtered_df = filtered_df.sort_values(
    by="Volume Numeric",
    ascending=False
)

top10 = filtered_df.head(10).copy()

top10.insert(
    0,
    "Volume Rank",
    range(1, len(top10) + 1)
)

top10.to_excel(
    "Task1_Python_Output.xlsx",
    index=False
)

print("\nTask 1 completed!")
print("Qualifying coins:", len(filtered_df))
print("\nTop 10:")
print(
    top10[
        [
            "Volume Rank",
            "Coin Name",
            "Symbol",
            "Volume (24h) USD"
        ]
    ]
)