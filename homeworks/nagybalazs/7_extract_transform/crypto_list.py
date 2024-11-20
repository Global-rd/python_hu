"""
A kövekező endpoint-ról “https://api.coingecko.com/api/v3/coins/markets”  húzd le a 250 legnagyobb market cap-pel rendelkező kriptovalutát 
(értelmezd az api dokumentációt, két paramétert kell összesen használnod, és 1 api hívásból megszerezhető az adat). 
*market cap = kibocsátott darabszám * ár
Dokumentáció: https://docs.coingecko.com/reference/coins-markets (figyelj hogy itt a url-ben “pro-api.coingecko.com” szerepel, 
neked viszont simán “api.coingecko.com” kell, így regisztráció nélkül használhatod az api-t.

Tárold el ezeket egy  dataframe-ben és oldd meg a következő feladatokat pandas segítségével:
 - Határozd meg, hogy a dataframe egyes oszlopaiban hány üres cella található és printeld ki.
 - Határozd meg a teljes dataframe-re a market_cap összegét és printeld ki.
 - Készíts egy új dataframe-et top50_df néven, itt csak az első 50 kriptovalutát tárold current_price alapján
 - Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő sorrendbe!
 - Hozz létre egy új oszlopot a top50_df-be change_direction néven amelynek 3 értéke lehet :
    - Ha a price_change_percentage_24h értéke nagyobb mint 0, az oszlop értéke legyen “+”
    - Ha negatív, az oszlop értéke legyen “-“
    - Ha kereken 0, az érték legyen “0”
"""

import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {  "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 250
         }
response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data)

empty_cells = df.isnull().sum()
print("Empty cells per column:\n", empty_cells)

total_market_cap = df["market_cap"].sum()
print("Total Market Cap:", total_market_cap)

top50_df = df.nlargest(50, "current_price")

top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)

def change_direction_definition(x):
    if x > 0:
        return "+"
    elif x < 0:
        return "-"
    else:
        return "0"

top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(change_direction_definition)

print(top50_df.head())

