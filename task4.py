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


# Clean 1-hour percentage change
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


# Assume 1-hour percentage is positive
df["Price Change"] = (
    df["Price (USD)"] * df["1h Change (%)"] / 100
)


# Price Range
df["Price Range"] = df["Price (USD)"].apply(
    lambda x: "Up to $10" if x < 10 else "$10 and above"
)


# Sort by Price Change
df = df.sort_values(
    by="Price Change",
    ascending=False
)


# Top 10
top10 = df.head(10)


# Save output
top10.to_excel(
    "Task4_Python_Output.xlsx",
    index=False
)


print("\nTask 4 Python completed!")
print(f"Top 10 coins: {len(top10)}")

print("\nTop 10:")
print(
    top10[
        [
            "Coin Name",
            "Symbol",
            "Price (USD)",
            "1h Change (%)",
            "Price Change",
            "Price Range"
        ]
    ].to_string(index=False)
)