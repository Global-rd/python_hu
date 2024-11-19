"""
Author: Gaál István Tamás
Task: Homework-7
"""
import requests
import pandas as pd
import json

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {"vs_currency": "usd",
          "order=": "market_cap_desc",
          "per_page": 250,}

with open("homeworks/gaalistvantamas/7_extract_transform/coins.json", "w") as file:
    cripto_coins = requests.get(url=url, params=params).json()
    file.write(json.dumps(cripto_coins))

df = pd.read_json("homeworks/gaalistvantamas/7_extract_transform/coins.json")
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#    print(df)
# 1. 
df_Nan = pd.DataFrame(df).count()
print("\n1...........")
print(250-df_Nan)

# 2. 
market_cap_sum = df["market_cap"].sum()
print("\n2...........")
print(market_cap_sum)

# 3.
top_50_df = pd.DataFrame(df.sort_values(by="current_price",ascending=False).head(50))
print("\n3...........")
print(top_50_df[["id", "current_price"]])

# 4.
top_50_df = pd.DataFrame(top_50_df.sort_values(by="price_change_percentage_24h",ascending=False))
print("\n4...........")
print(top_50_df[["id", "price_change_percentage_24h"]])

# 5.
def change_direction_index(row):
    if row["price_change_percentage_24h"] == 0 and row["price_change_percentage_24h"] < 1:
        return "0"
    elif  row["price_change_percentage_24h"] > 1:
        return "+"
    else:
        return "-"
    
top_50_df["change_direction"] = top_50_df.apply(change_direction_index, axis=1)
print("\n5...........")
print(top_50_df[["id", "price_change_percentage_24h", "change_direction"]])