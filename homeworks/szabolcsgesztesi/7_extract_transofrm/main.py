import requests
import pandas as pd

# API endpoint és paraméterek
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",  # Az árakat USD-ban kérjük
    "order": "market_cap_desc",  # Legnagyobb market cap először
    "per_page": 250,  # 250 legnagyobb kriptovaluta
    "page": 1  # Az első oldal
}

# Az API hívás
response = requests.get(url, params=params)
data = response.json()

# A válasz átalakítása DataFrame-be
df = pd.DataFrame(data)

# 1. Feladat - Üres cellák száma az oszlopokban
print("Üres cellák száma az oszlopokban:")
print(df.isna().sum())

# 2. Feladat - Market cap összege
total_market_cap = df['market_cap'].sum()
print(f"\nA teljes market cap összeg: {total_market_cap}")

# 3. Feladat - Top 50 kriptovaluta
top50_df = df.head(50)

# 4. Feladat - Top50_df-t price_change_percentage_24h alapján csökkenő sorrendbe rendezve
top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)

# 5. Feladat - Change direction oszlop hozzáadása

def determine_change_direction(x):
    if x > 0:
        return "+"
    elif x < 0:
        return "-"
    else:
        return "0"

top50_df['change_direction'] = top50_df['price_change_percentage_24h'].apply(determine_change_direction)

# 5.Feladat eredményének kiíratása
print("\nTop 50 kriptovaluta a price_change_percentage_24h szerint rendezve:")
print(top50_df[['id', 'current_price', 'price_change_percentage_24h', 'change_direction']])