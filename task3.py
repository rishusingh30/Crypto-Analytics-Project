import pandas as pd

file_path = "Crypto_Analytics_Project(1).xlsm"

# Load Raw Data
df = pd.read_excel(
    file_path,
    sheet_name="Raw Data"
)

print(f"Raw Data loaded: {len(df)} rows")


# Clean Price
df["Price (USD)"] = (
    df["Price (USD)"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)

df["Price (USD)"] = pd.to_numeric(
    df["Price (USD)"],
    errors="coerce"
)


# Clean Volume
df["Volume (24h) USD"] = (
    df["Volume (24h) USD"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)

df["Volume (24h) USD"] = pd.to_numeric(
    df["Volume (24h) USD"],
    errors="coerce"
)


# Price Category
df["Price Category"] = df["Price (USD)"].apply(
    lambda x: "$0-$50" if x <= 50 else "Above $50"
)


# Sort by Volume
df = df.sort_values(
    by="Volume (24h) USD",
    ascending=False
)


# Top 5 from each category
top5 = (
    df.groupby(
        "Price Category",
        group_keys=False
    )
    .head(5)
)


# Save output
top5.to_excel(
    "Task3_Python_Output.xlsx",
    index=False
)


print("\nTask 3 Python completed!")
print(f"Top 5 coins selected: {len(top5)}")

print("\nTop 5:")
print(
    top5[
        [
            "Coin Name",
            "Symbol",
            "Price (USD)",
            "Volume (24h) USD",
            "Price Category"
        ]
    ].to_string(index=False)
)