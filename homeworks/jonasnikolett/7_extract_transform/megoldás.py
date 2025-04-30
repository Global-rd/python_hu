"""
Tárold el ezeket egy  dataframe-ben és oldd meg a következő feladatokat pandas segítségével:
1.	Határozd meg, hogy a dataframe egyes oszlopaiban hány üres cella található és printeld ki.
2.	Határozd meg a teljes dataframe-re a market_cap összegét és printeld ki.
3.	Készíts egy új dataframe-et top50_df néven, itt csak az első 50 kriptovalutát tárold current_price alapján
4.	Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő sorrendbe!
5.	Hozz létre egy új oszlopot a top50_df-be change_direction néven amelynek 3 értéke lehet :
        a.	Ha a price_change_percentage_24h értéke nagyobb mint 0, az oszlop értéke legyen “+”
        b.	Ha negatív, az oszlop értéke legyen “-“
        c.	Ha kereken 0, az érték legyen “0”


"""

import pandas as pd

print("1 Határozd meg, hogy a dataframe egyes oszlopaiban hány üres cella található és printeld ki.")
df = pd.read_csv("homeworks/jonasnikolett/7_extract_transform/list_250.csv")
empty_cells_per_column_df = df.isnull().sum()

print(empty_cells_per_column_df)
print("_____________________________________________________________________________________________")
print("2. Határozd meg a teljes dataframe-re a market_cap összegét és printeld ki.")

total_market_cap_df = df["market_cap"].sum()
print(total_market_cap_df)
print("_____________________________________________________________________________________________")
print("3. Készíts egy új dataframe-et top50_df néven, itt csak az első 50 kriptovalutát tárold current_price alapján")

top50_df = df.sort_values("current_price", ascending=False).head(50)
print(top50_df)
print("_____________________________________________________________________________________________")
print("4. .	Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő sorrendbe!")

top50_df = top50_df.sort_values("price_change_percentage_24h", ascending=False)
print(top50_df)

print("_____________________________________________________________________________________________")
print("5. Hozz létre egy új oszlopot a top50_df-be change_direction néven....")

def change_direction_column(row):
    if row["price_change_percentage_24h"] > 0:
        return "+"
    elif row["price_change_percentage_24h"] < 0:
        return "-"
    else:
        return "0"
top50_df["change_direction"] = top50_df.apply(change_direction_column, axis=1)
print(top50_df)
print("_____________________________________________________________________________________________")
