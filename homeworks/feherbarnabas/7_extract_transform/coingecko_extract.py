import requests
import pandas as pd

#API letöltése
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",  
    "order": "market_cap_desc", 
    "per_page": 250, 
    "page": 1  
}
response = requests.get(url, params=params)
data = response.json()

#DataFrame létrehozása
df = pd.DataFrame(data)

#Üres cellák száma az oszlopokban
empty_cells = df.isnull().sum()
print("Üres cellák száma oszloponként:\n", empty_cells)

#A market_cap oszlop összegzése
total_market_cap = df["market_cap"].sum()
print("A teljes market_cap összege:", total_market_cap)

#Top 50 kriptovaluta kiválasztása current_price alapján
top50_df = df.nlargest(50, "current_price")

#Top 50 kriptovaluta rendezése price_change_percentage_24h alapján
top50_df = top50_df.sort_values(
    by="price_change_percentage_24h", ascending=False)

# Új oszlop létrehozása change_direction néven
def change_direction(price_change):
    if price_change > 0:
        return "+"
    elif price_change < 0:
        return "-"
    else:
        return "0"

top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(change_direction)

# 8. Eredmény printelése
print("Top 50 kriptovaluta (current_price alapján):\n", top50_df)
