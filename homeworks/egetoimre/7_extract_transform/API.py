import pandas as pd
import requests

url = "https://api.coingecko.com/api/v3/coins/markets"
parameter = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 250,
    "page": 1
}

response = requests.get(url, params=parameter)
data = response.json()

Frame = pd.DataFrame(data)

print(Frame.isnull().sum())

total_market = Frame['market_cap'].sum()
print("Összes piac:", total_market)

TOT_50_frame = Frame.head(50).copy()

TOT_50_frame.sort_values(by='price_change_percentage_24h', ascending=False, inplace=True)

def get_change_direction(row):
    if row['price_change_percentage_24h'] > 0:
        return "+"
    elif row['price_change_percentage_24h'] < 0:
        return "-"
    else:
        return "0"

TOT_50_frame['change_direction'] = TOT_50_frame.apply(get_change_direction, axis=1)

print(TOT_50_frame)