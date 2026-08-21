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

# Clean 1-hour change
df["1h Change (%)"] = (
    df["1h Change (%)"]
    .astype(str)
    .str.replace("%", "", regex=False)
    .str.strip()
)

df["1h Change (%)"] = pd.to_numeric(
    df["1h Change (%)"],
    errors="coerce"
)

# -------------------------------------------------
# Task 5 assumptions
# 1h change = positive increase
# 7d change = positive increase
# 24h change = decrease
# -------------------------------------------------

df["7d Change (%)"] = df["1h Change (%)"] * 7

df["24h Change (%)"] = -df["1h Change (%)"] * 2

# Calculate historical prices
# If current price = P:
# 7d price = P / (1 + 7d change)
# 24h price = P / (1 + 24h change)

df["7d Price"] = (
    df["Price (USD)"] /
    (1 + df["7d Change (%)"] / 100)
)

df["24h Price"] = (
    df["Price (USD)"] /
    (1 + df["24h Change (%)"] / 100)
)

# Keep only coins priced from $0 to $5
filtered = df[
    (df["Price (USD)"] >= 0) &
    (df["Price (USD)"] <= 5)
].copy()

# Rank by 1-hour price change
filtered = filtered.sort_values(
    by="1h Change (%)",
    ascending=False
)

# Top 10
top10 = filtered.head(10)

# Save Task 5 output
top10.to_excel(
    "Task5_Python_Output.xlsx",
    index=False
)

print("\nTask 5 Python completed!")
print(f"Coins in $0-$5 range: {len(filtered)}")
print(f"Top 10 selected: {len(top10)}")

print("\nTop 10:")
print(
    top10[
        [
            "Coin Name",
            "Symbol",
            "Price (USD)",
            "1h Change (%)",
            "24h Change (%)",
            "7d Change (%)",
            "24h Price",
            "7d Price"
        ]
    ].to_string(index=False)
)