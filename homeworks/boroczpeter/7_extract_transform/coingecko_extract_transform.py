import requests
import pandas as pd

# URL of the API
url = "https://api.coingecko.com/api/v3/coins/markets"

# parameters settings
params = {
    "vs_currency": "usd", #compulsory data
    "order": "market_cap_dsc", # should be descending in order to specify the highest value of a cryptocurrency
    "per_page": 250,
    "page": 1,
}

# getting the parameters from the API
data = requests.get(url, params=params).json()
df = pd.DataFrame(data)

# 1. determine and print the empty cells in the coloumns            OK
missing_values = df.isna().sum()
print("Empty fields in the columns:")
print(missing_values)
print("--------------------------------------------")

# 2. Sum of the market caps and print                OK
sum_all_market_cap = df["market_cap"].sum()
print("Total market capitalization (USD):")
print(sum_all_market_cap)
print("--------------------------------------------")

# 3. new dataframe for the top 50 sorted in current_price
top50_df = df.sort_values("current_price", ascending=False).head(50)
#print(top50_df[["name", "current_price"]])
#print("--------------------------------------------")

# 4. sorting the top50_df per price_change_percentage_24h
top50_df_sort_by_pcp24 = top50_df.sort_values("price_change_percentage_24h", ascending=False)
#print(top50_df_sort_by_pcp24)
#print("--------------------------------------------")

# 5. adding an extra column change_direction to top50_df and determine the value of it
top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(
    lambda value: "+" if value > 0 else "-" if value < 0 else "0"
)
#print (top50_df[["name","price_change_percentage_24h", "change_direction"]])