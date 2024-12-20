import pandas as pd
import requests

def change_direction(row):
    if row > 0:
        return "+"
    elif row < 0:
        return "-"
    else:
        return "0"

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 250,
    'page': 1
}

response = requests.get(url, params=params)
data = response.json()
df = pd.DataFrame(data)
df.to_csv('E:/Tanfolyam/python_hu/homeworks/debreczenizoltan/7_extract_transform/crypto_data.csv', index=False)
print(df.isnull().sum())

total_market_cap = df['market_cap'].sum()
print(f"Total Market Cap: {total_market_cap}")

top50_df = df.nlargest(50, 'current_price')

top50_df = top50_df.sort_values(by='price_change_percentage_24h', ascending=False)

top50_df['change_direction'] = top50_df['price_change_percentage_24h'].apply(change_direction)

top50_df.to_csv('E:/Tanfolyam/python_hu/homeworks/debreczenizoltan/7_extract_transform/top50_crypto_data.csv', index=False)

