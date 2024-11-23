"""
market_cap.py --- Asztalos Lajos --- 2024.11.16
"""

import requests
import pandas as pd


url = "https://api.coingecko.com/api/v3/coins/markets"
params = {"vs_currency": "EUR",
          "order": "market_cap_desc",
          "per_page": "250"}
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers, params=params).json()

df=pd.DataFrame(response)

#Az üres cellák száma oszloponként
#empty_cells_per_column = df.isnull().sum().reset_index()
print("Az üres cellák száma oszloponként")
print("-----------------------------------------")
print(df.isnull().sum().reset_index())
print("-----------------------------------------\n")
#A market_cap összege a teljes dataframere
#sum_market_cap = df["market_cap"].sum()
print(f"A tözsdei kapitalizáció összesen: {df["market_cap"].sum():,} EUR\n")

#Az első 50 kriptovaluta ár szerint növekvő sorrendben
print("Az első 50 kriptovaluta, ár szerint növekvő sorrendben")
top50_df = df.sort_values(by="current_price", ascending=True).head(50)
print(top50_df)

#Az első 50 kriptovaluta a 24 órás százalékos árváltozás szerint csökkenő sorrendben 
top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)
#print(top50_df)

#Az új mező feltétel szerinti értékmeghatározása
def categorize_stock(row):
    if row["price_change_percentage_24h"] > 0:
        return '+'
    elif row["price_change_percentage_24h"] < 0:
        return '-'
    else: return "0"

#Az első 50 kriptovaluta dataframje kiegészítve a változási irány szimbolum mezővel
top50_df["change_direction"] = top50_df.apply(categorize_stock, axis=1)
#print(top50_df)
#print(top50_df.price_change_percentage_24h)