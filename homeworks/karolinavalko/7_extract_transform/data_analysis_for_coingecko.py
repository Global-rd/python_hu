import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {"vs_currency": "sek", "per_page": 250}

response = requests.get(url=url, params=params).json()

df = pd.DataFrame(response)

null_cells = df.isnull().sum()
print(null_cells)

total_market_cap = df["market_cap"].sum()
print("Total market cap is:", total_market_cap)

top50_df = df.nlargest(50, ["current_price"]).sort_values("price_change_percentage_24h", ascending = False)

def categorize_price_change_percantage_24h (row):
    if row["price_change_percentage_24h"] > 0:
        return "+"
    elif row["price_change_percentage_24h"] < 0:
        return "-"
    elif row["price_change_percentage_24h"] == 0:
        return "0"
    
top50_df["change direction"] = top50_df.apply(categorize_price_change_percantage_24h, axis=1)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(top50_df)