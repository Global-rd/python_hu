import requests
import settings as s
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {"accept": "application/json",
          "x-cg-demo-api-key": s.COINGECKO_API_KEY,
          "vs_currency": "usd",
          "per_page": "250",
          "page": "1"}

response = requests.get(url=url, params=params).json()

df = pd.DataFrame(response)
print(df)
print(df.info())

# 1. Define the number of empty (isnull) cells in each columns
empty_cells = df.isnull().sum()
print(empty_cells)

# 2. Total market cap
total_market_cap = df["market_cap"].sum()
formatted_total_market_cap = "{:,.0f}".format(total_market_cap)
print(formatted_total_market_cap)

# 3. Top 50 based on current price
top_50_df = df.nlargest(50, 'current_price')

# 4. Sort descending Top50 by price_change_percentage_24h
top_50_df_sorted_by_price_change_percentage_24_desc = top_50_df.sort_values('price_change_percentage_24h', ascending=False)
print(top_50_df_sorted_by_price_change_percentage_24_desc)

# 5. New column (change_direction) in top_50_df (3 possible values: + / - / 0)
def change_direction(row):
    if row['price_change_percentage_24h'] > 0:
        return '+'
    elif row['price_change_percentage_24h'] < 0:
        return '-'
    else:
        return '0'
    
top_50_df['change_direction'] = top_50_df.apply(change_direction, axis=1)
print(top_50_df[['name', 'price_change_percentage_24h', 'change_direction']])