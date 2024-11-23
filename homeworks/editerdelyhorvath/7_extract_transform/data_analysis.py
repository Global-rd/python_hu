'''

7. házi feladat
A CoinGecko API-val kinyert adatok elemzése Pandas-szal.

- Tárold el ezeket egy  dataframe-ben
- Határozd meg, hogy a dataframe egyes oszlopaiban hány üres cella található és printeld ki.
- Határozd meg a teljes dataframe-re a market_cap összegét és printeld ki.
- Készíts egy új dataframe-et top50_df néven, itt csak az első 50 kriptovalutát tárold current_price alapján
- Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő sorrendbe!
- Hozz létre egy új oszlopot a top50_df-be change_direction néven amelynek 3 értéke lehet :
    - Ha a price_change_percentage_24h értéke nagyobb mint 0, az oszlop értéke legyen “+”
    - Ha negatív, az oszlop értéke legyen “-“
    - Ha kereken 0, az érték legyen “0”

'''


from coingecko_extraction import CoinGeckoAPI  
import pandas as pd


####################  Get Data from CoinGecko API  ####################
api = CoinGeckoAPI(vs_currency="usd", order="market_cap_desc", per_page=250, page=1)
data = api.fetch_data()


# Store the data in a dataframe
df = pd.DataFrame(data)

# How many empty cells are in each column of the dataframe (print them)
missing_values = df.isnull().sum()
print(f"Empty cells in the columns: \n{missing_values}")

# Print the sum of market_cap for the whole dataframe
total_market_cap = df["market_cap"].sum()
print(f"\n###########################\nSUM of the market_cap: {total_market_cap:,} USD")

# top50_df for the first 50 cryptocurrencies stored in current_price
top50_df = df.nlargest(50, 'current_price')

# sorting by price_change_percentage_24h
top50_df = top50_df.sort_values('price_change_percentage_24h', ascending=False).reset_index(drop=True)
top50_df.index = top50_df.index + 1
print(f"\n###########################\nTop 5 cryptocurrencies stored by current_price: \n{top50_df[['name', 'current_price', 'price_change_percentage_24h']].head()}")

# adding change_direction column
def determine_change_direction(value):
    if value > 0:
        return "+"
    elif value < 0:
        return "-"
    else:
        return "0"

top50_df['change_direction'] = top50_df['price_change_percentage_24h'].apply(determine_change_direction)
print(f"\n###########################\nTop 5 cryptocurrencies with the new change_direction column: \n{top50_df[['name', 'current_price', 'price_change_percentage_24h', 'change_direction']].head()}")



