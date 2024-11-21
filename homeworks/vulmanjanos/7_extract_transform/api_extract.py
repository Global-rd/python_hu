
import requests
import pandas as pd

# Adatlekérés: CoinGecko API
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 250,
    "page": 1
}
response = requests.get(url, params=params)
data = response.json()

# DataFrame adattárolás
df = pd.DataFrame(data)

# Üres cella meghatározás oszloponként
empty_cells = df.isnull().sum()
print("Oszloponkénti üres cellák:\n", empty_cells)

# Market cap összeg
total_market_cap = df['market_cap'].sum()
print("Total market cap összeg:", total_market_cap)

# 3. Első 50 kriptovaluta jelenlegi ár alapján, új DataFrame létrehozás
top50_df = df.nlargest(50, 'current_price')

# 4. A top50_df price_change_percentage_24h alapján csökkenő sorrendbe rendezáse
top50_df = top50_df.sort_values(by='price_change_percentage_24h', ascending=True)

# 5. Egy új, change direction nevű oszlop létrehozása
top50_df['change_direction'] = top50_df['price_change_percentage_24h'].apply(
    lambda x: '+' if x > 0 else ('-' if x < 0 else '0')
)

print(top50_df)
