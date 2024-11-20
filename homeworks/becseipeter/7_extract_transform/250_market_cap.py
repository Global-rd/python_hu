import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

data = response.json()  
limited_data = data[:250]  # Get only the first 250 items 
print(limited_data)

df = pd.DataFrame(limited_data)

#################################################################################

empty_cells = df.isnull().sum()   #Define of empty cell in colums
print(empty_cells)

sum_market_cap = df["market_cap"].sum()    #The sum of the market_cap for the entire dataframe
print(sum_market_cap)

top50_df = df.sort_values("current_price", ascending=False).head(50)     #Top 50 cryptocurrencies in ascending order by price
print(top50_df)

top50_df_24h = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)   #Top 50 cryptocurrencies price in 24 hours in descending order
print(top50_df_24h)

def new_change_direction(column):                     #New columns with 3 value     
    if column["price_change_percentage_24h"] > 0:
        return '+'
    elif column["price_change_percentage_24h"] < 0:
        return '-'
    else: return "0"

