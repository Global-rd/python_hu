import requests
import pandas as pd


class ApiConnect:
    def __init__(self, url):
        self.base_url = url

    def get_data(self, params):
        api_data = []
        url = self.base_url  
        while url:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                result = response.json()
                api_data.extend(result)
                if len(result) < params["per_page"]:
                    break
                params["page"] += 1
            else:
                print(f"Error {response.status_code}: {response.json().get('error', 'Unknown error')}")
                break
        return api_data

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "per_page": 250,
    "page": 1
}

api = ApiConnect(url)
api_data = api.get_data(params)
#print(api_data)

df = pd.DataFrame(api_data)

print(df)

print(df.info())

#1. empty cells:
empty_cells = df.isnull().sum()
print(empty_cells)

# 2. Total market cap
total_market_cap = df["market_cap"].sum()
format_total_market_cap = "{:,.0f}".format(total_market_cap)
print(format_total_market_cap)

# 3. Top 50 krypto
top_50_df = df.nlargest(50, 'current_price')

# 4. Sorted top50
top_50_df_sorted = top_50_df.sort_values('price_change_percentage_24h', ascending=False)
print(top_50_df_sorted)

# 5. New column with conditionals:
def change_direction(row):
    if row['price_change_percentage_24h'] > 0:
        return '+'
    elif row['price_change_percentage_24h'] < 0:
        return '-'
    else:
        return '0'
    
top_50_df['change_direction'] = top_50_df.apply(change_direction, axis=1)
print(top_50_df[['name', 'price_change_percentage_24h', 'change_direction']])