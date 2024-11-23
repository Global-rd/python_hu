"""
- OK Hozz létre egy új mappát a neveddel ellátott mappán belül “7_extract_transform” néven.
- OK A következő feladatokhoz tartozó .py file-okat ide mentsd el.
- OK A következő feladatban a coinGecko public API-járól kell majd adatokat kinyerned, és ezeket elemezni Python segítségével. 
- OK A kövekező endpoint-ról “https://api.coingecko.com/api/v3/coins/markets”  húzd le a 250 legnagyobb market cap-pel rendelkező kriptovalutát (értelmezd az api dokumentációt, két paramétert kell összesen használnod, és 1 api hívásból megszerezhető az adat). *market cap = kibocsátott darabszám * ár
- OK Dokumentáció: https://docs.coingecko.com/reference/coins-markets (figyelj hogy itt a url-ben “pro-api.coingecko.com” szerepel, neked viszont simán “api.coingecko.com” kell, így regisztráció nélkül használhatod az api-t.

- OK Tárold el ezeket egy dataframe-ben és oldd meg a következő feladatokat pandas segítségével:
- OK Határozd meg, hogy a dataframe egyes oszlopaiban hány üres cella található és printeld ki.
- OK Határozd meg a teljes dataframe-re a market_cap összegét és printeld ki.
- OK Készíts egy új dataframe-et top50_df néven, itt csak az első 50 kriptovalutát tárold current_price alapján
- OK Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő sorrendbe!
- OK Hozz létre egy új oszlopot a top50_df-ben change_direction néven, amelynek 3 értéke lehet
    > Ha a price_change_percentage_24h értéke nagyobb mint 0, az oszlop értéke legyen “+”
    > Ha negatív, az oszlop értéke legyen “-“
    > Ha kereken 0, az érték legyen “0”
"""

import requests
import pandas as pd
import os
from datetime import datetime

### I. BLOKK: ########################################################################
### Függvény definiálása API kapcsolathoz#############################################
######################################################################################
def get_top250_cryptocurr():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    # Az alábbi paramétereket ez alapján a dokumentáció állítottam be (nem volt egyszerű megtalálni :))
    # https://docs.coingecko.com/v3.0.1/docs/1-get-data-by-id-or-address#other-way-to-obtain-coin-prices--market-data
    params = {
    "vs_currency": "usd",           # USD beállítása valutaként
    "order": "market_cap_desc",     # market cap csökkenő sorrend beállítása
    }
    response = requests.get(url=url, params=params)
    # Itt "slice"-al vágom le az első 250 értéket, így fentebb csak 2 paramétert hozok be, a feladat szerint,
    # és nem ott definiálom a "per_page": 250 és a "page": 1 paraméterek megadásával
    return response.json()[0:250]  


### Kiegészítés: a program futásakor a képernyő törlése ###
current_datetime = datetime.now()
os.system("cls")
print(f"====== Előző futási eredmény törölve a képernyőről ekkor: {current_datetime}) ======")
print("------------------------------------------------------------------")



### II. BLOKK: #######################################################################
### Függvény hívása, top250 érték tárolása DataFrame-ben #############################
######################################################################################
top_250 = get_top250_cryptocurr()
df = pd.DataFrame(top_250)
#print(df.dtypes)
#print(df)



# Határozd meg, hogy a dataframe egyes oszlopaiban hány üres cella található és printeld ki.
sum_blank_cells = df.isnull().sum().reset_index()
print(f"Total no. of empty cells by column:\n{sum_blank_cells}")
print("------------------------------------------------------------------")



# Határozd meg a teljes dataframe-re a market_cap összegét és printeld ki.
    # int64 típus, további számításokhoz:
sum_matket_cap = df["market_cap"].sum()

    #string típus, olvashatóbb megjelenítésért:
sum_matket_cap_formatted = '{:,}'.format(sum_matket_cap).replace(",", ".")

print(f"Total market capitalization:\nUSD {sum_matket_cap_formatted}")
print("------------------------------------------------------------------")



# Készíts egy új dataframe-et top50_df néven, itt csak az első 50 kriptovalutát tárold current_price alapján
    # !!! Itt az eredeti top250-es listát előbb sroba rendeztem current_price alapján, majd ebből tároltam le a top50-t
top50_df = df.sort_values(by="current_price", ascending=False).head(50).reset_index()
columns_to_display = ["id", "name", "current_price", "price_change_percentage_24h"]
print(f"Top 50 new cryptos by current_price:\n{top50_df[columns_to_display]}")
print("------------------------------------------------------------------")



# Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő sorrendbe!
top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False).reset_index()
columns_to_display2 = ["id", "name", "price_change_percentage_24h"]
print(f"Top 50 new cryptos by price_change_percentage_24h:\n{top50_df[columns_to_display2]}")
print("------------------------------------------------------------------")



# Hozz létre egy új oszlopot a top50_df-ben change_direction néven, amelynek 3 értéke lehet
   # > Ha a price_change_percentage_24h értéke nagyobb mint 0, az oszlop értéke legyen “+”
   # > Ha negatív, az oszlop értéke legyen “-“
   # > Ha kereken 0, az érték legyen “0”
def change_direction_rule(v):
    if v > 0:
        return "+"
    elif v < 0:
        return "-"
    else:
        return 0

top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(change_direction_rule)
columns_to_display3 = ["id", "name", "price_change_percentage_24h", "change_direction"]
print(f"Top 50 cryptos' price change:\n{top50_df[columns_to_display3]}")
print("------------------------------------------------------------------")