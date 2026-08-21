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

# Clean 1h Change
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

# ------------------------------------------------
# Task 6 assumptions:
# 1h, 24h and 7d changes are treated as downfall %
# ------------------------------------------------

# We only have actual 1h Change in Raw Data.
# Use the same assumptions used in Task 5.

df["24h Change (%)"] = df["1h Change (%)"] * 2
df["7d Change (%)"] = df["1h Change (%)"] * 7

# Average downfall percentage
df["Average Downfall (%)"] = (
    df["1h Change (%)"]
    + df["24h Change (%)"]
    + df["7d Change (%)"]
) / 3

# Price ranges
def price_range(price):
    if price <= 0.05:
        return "$0-$0.05"
    elif price <= 0.5:
        return "$0.05-$0.5"
    elif price <= 5:
        return "$0.5-$5"
    elif price <= 50:
        return "$5-$50"
    else:
        return ">$50"


df["Price Range"] = df["Price (USD)"].apply(price_range)

# Find coin with lowest average downfall in each range
results = []

for price_range_name in [
    "$0-$0.05",
    "$0.05-$0.5",
    "$0.5-$5",
    "$5-$50",
    ">$50"
]:

    selected = df[
        df["Price Range"] == price_range_name
    ].copy()

    if len(selected) > 0:

        best_coin = selected.loc[
            selected["Average Downfall (%)"].idxmin()
        ]

        results.append({
            "Price Range": price_range_name,
            "Coin Name": best_coin["Coin Name"],
            "Symbol": best_coin["Symbol"],
            "Price (USD)": best_coin["Price (USD)"],
            "Average Downfall (%)": best_coin["Average Downfall (%)"],
            "Total Coins": len(selected)
        })

# Create final KPI table
result_df = pd.DataFrame(results)

# Save output
result_df.to_excel(
    "Task6_Python_Output.xlsx",
    index=False
)

print("\nTask 6 Python completed!")

print("\nKPI Results:")
print(result_df.to_string(index=False))