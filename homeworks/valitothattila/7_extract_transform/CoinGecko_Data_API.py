import requests
import pandas as pd

# ----------------------------------- API paraméterek -----------------------------------
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "eur",                           # pénznem
    "per_page": 250,                                # 250 legnagyobb market cap
    "order": "market_cap_desc",                     # rendezés beállítása
    "page": 1                                       # lista kezdete
}

# -----------------------------------  API hívás 
response = requests.get(url, params=params)
cripto_list_data = response.json()

# ----------------------------------- DataFrame létrehozása 
df = pd.DataFrame(cripto_list_data)

#print(df)

# ----------------------------------- 1. Üres cellák száma oszloponként 
empty_cell_no = (df.isna().sum())
print(f"\nÜres cellák száma:\n{empty_cell_no}")

# ----------------------------------- 2. Határozd meg a teljes dataframe-re a market_cap összegét és printeld ki

tot_m_cap = df['market_cap'].sum()
print(f"\nTotál market cap összegezve: {tot_m_cap}")

# ----------------------------------- 3. Új dataframe csak az első 50 kriptovalutát tárold current_price alapján
top50_df = df.nlargest(50, "current_price")

# ----------------------------------- 4. Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő sorrendbe!
top50_df = top50_df.sort_values(by="price_change_percentage_24h",ascending=False)
print("\nTop50_df price_change_percentage_24h alapján csökkenő sorrendben:")
print(top50_df)

# --------------- 5. Hozz létre egy új oszlopot a top50_df-be change_direction néven amelynek 3 értéke lehet : "+", "-"; "0"
def detect_direction(price_change_perc):
        if price_change_perc > 0:
            return "+"
        elif price_change_perc < 0:
            return "-"
        else:
            return "0"

top50_df['change_direction'] = top50_df['price_change_percentage_24h'].apply(detect_direction)
    
print("\nTop 50 kriptovaluta, rendezve 'price_change_percentage_24h' oszlop szerint:")
print(top50_df[['name', 'symbol', 'current_price', 'market_cap', 'price_change_percentage_24h', 'change_direction']])





