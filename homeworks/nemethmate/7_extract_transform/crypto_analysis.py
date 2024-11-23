import requests
import pandas as pd

# CoinGecko API URL
API_URL = "https://api.coingecko.com/api/v3/coins/markets"

# Paraméterek az API híváshoz
params = {
    "vs_currency": "usd",  # Az árfolyamokat USD-ben adjuk meg
    "order": "market_cap_desc",  # Market cap szerint csökkenő sorrendben
    "per_page": 250,  # 250 kriptovalutát kérünk le
    "page": 1,  # Csak az első oldalt kérjük
}

# Adatok lekérése az API-ról
response = requests.get(API_URL, params=params)
if response.status_code != 200:
    raise Exception(f"API request failed with status code {response.status_code}")
    
# JSON adat betöltése
data = response.json()

# Adatok átalakítása DataFrame-be
df = pd.DataFrame(data)

# 1. Üres cellák száma oszloponként
print("Missing values per column:")
print(df.isnull().sum())

# 2. Market cap összegének kiszámítása
total_market_cap = df["market_cap"].sum()
print(f"\nTotal market cap: ${total_market_cap:,.2f}")

# 3. Top 50 kriptovaluta kiválasztása current_price alapján
top50_df = df.nlargest(50, "current_price").copy()

# 4. Rendezzük a top50_df-et price_change_percentage_24h alapján csökkenő sorrendbe
top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)

# 5. Új oszlop létrehozása change_direction néven
def determine_change_direction(change):
    if change > 0:
        return "+"
    elif change < 0:
        return "-"
    else:
        return "0"

top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(determine_change_direction)

# Top 50 DataFrame megtekintése
print("\nTop 50 cryptocurrencies:")
print(top50_df[["name", "current_price", "price_change_percentage_24h", "change_direction"]].head())
