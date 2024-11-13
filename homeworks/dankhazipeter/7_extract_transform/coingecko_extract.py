import requests
import pandas as pd

# Adatok lekérése a CoinGecko API-ról
URL = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 250,
    'page': 1
}

response = requests.get(URL, params=params, timeout=10)
data = response.json()

# DataFrame létrehozása a lekért adatokból
df = pd.DataFrame(data)

# Határozd meg, hogy hány üres cella van az egyes oszlopokban
empty_cells = df.isnull().sum()
print("Üres cellák száma az egyes oszlopokban:")
print(empty_cells)

# Számítsd ki és printeld ki a teljes market cap-et
total_market_cap = df['market_cap'].sum()
print("Teljes market cap:", total_market_cap)

# Hozz létre egy új DataFrame-et top50_df néven, az első 50 kriptovalutával current_price alapján
top50_df = df.nlargest(50, 'current_price')

# Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő sorrendbe
top50_df = top50_df.sort_values(
    by='price_change_percentage_24h', ascending=False)


def change_direction(row):
    """
    Meghatározza az árfolyamváltozás irányát.

    Args:
        row (float): Az árfolyam változása százalékban az elmúlt 24 órában.

    Returns:
        str: '+' ha az árfolyam emelkedett, '-' ha csökkent, '0' ha nem változott.
    """
    if row > 0:
        return '+'
    elif row < 0:
        return '-'
    else:
        return '0'


# Hozz létre egy új oszlopot 'change_direction' néven, amely értékei '+', '-', vagy '0'
top50_df['change_direction'] = top50_df['price_change_percentage_24h'].apply(
    change_direction)

# Az eredményül kapott DataFrame megjelenítése
top50_df.reset_index(drop=True, inplace=True)
print(top50_df)
