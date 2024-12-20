import pandas as pd
from coingecko_api import CoinGecko


df = pd.DataFrame(CoinGecko.get_data("markets", "usd", 250))
#Határozd meg, hogy a dataframe egyes oszlopaiban hány üres cella található és printeld ki.
df.info() # -> max_supply 143, roi 32 // de ez még nem számolja meg az üres cellákat!!
#itt végig kellene loopolni az összes oszlopon és megszámolni a NaN / None / "" értékeket??
#count_null_values = df[df["roi"] == "None"] pl ennek a típusa object...

#Határozd meg a teljes dataframe-re a market_cap összegét és printeld ki.
#print(df[["name", "market_cap"]])
total_market_cap = df["market_cap"].sum()
print(f"Total market cap: {total_market_cap}")

#Készíts egy új dataframe-et top50_df néven, itt csak az első 50 kriptovalutát tárold current_price alapján
top50_df = df.sort_values("current_price", ascending=True).head(50)
#print(top50_df[["name", "current_price"]])

#Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő sorrendbe!
top50_df.sort_values("price_change_percentage_24h", ascending=False)
#print(top50_df[["name", "price_change_percentage_24h"]])

#Hozz létre egy új oszlopot a top50_df-be change_direction néven amelynek 3 értéke lehet :
#        Ha a price_change_percentage_24h értéke nagyobb mint 0, az oszlop értéke legyen “+”
#        Ha negatív, az oszlop értéke legyen “-“
#        Ha kereken 0, az érték legyen “0”
def categorize_price_change(row):
    if row["price_change_percentage_24h"] > 0:
        return "+"
    elif row["price_change_percentage_24h"] < 0:
        return "-"
    else: 
        return "0"

top50_df["change_direction"] = top50_df.apply(categorize_price_change, axis=1)
print(top50_df[["name", "price_change_percentage_24h", "change_direction"]])