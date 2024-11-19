import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    'vs_currency': 'usd',  # Az árak USD-ben
    'order': 'market_cap_desc',  # Csökkenő sorrend a kibocsátott darabszám szerint
    'per_page': 250,  # 250 elem, market_cap_desc csökkenő sorrend miatt a legnagyobb darabszámban kiadottak
    'page': 1,  # Az első oldalt kéri le
}

# API hívás
response = requests.get(url, params=params)

# Ellenőrizzük a válasz státuszát
if response.status_code == 200:
    data = response.json()  # JSON formátumban kapott válasz dekódolása

    # Átkonvertáljuk a kapott adatokat pandas DataFrame-be
    df = pd.DataFrame(data)

    # Csak a szükséges oszlopok kiválasztása
    df = df[['name', 'symbol', 'current_price', 'market_cap', 'price_change_percentage_24h']]

    # Oszlopok átnevezése
    df=df.rename(columns={'name':'Név', 'symbol':'Szimbólum','current_price':'Ár (USD)','market_cap':'Piaci kapitálizáció',
    'price_change_percentage_24h':'24h Árfolyamváltozás (%)'})
    
    # 1. Határozd meg, hogy a DataFrame egyes oszlopaiban hány üres cella található és printeld ki
    missing_values = df.isna().sum()
    print(" ")
    print("\n--- 1. ---")
    print("\nÜres cellák száma oszloponként:")
    print(missing_values)

    # 2. Határozd meg a teljes DataFrame-re a market_cap összegét és printeld ki
    total_market_cap = df['Piaci kapitálizáció'].sum()
    print("\n--- 2. ---")
    print(f"\nÖsszes Piaci kapitálizáció: {total_market_cap} (USD)")

    # 3. Készíts egy új DataFrame-et top50_df néven, itt csak az első 50 kriptovalutát tárold current_price alapján
    top50_df = df.nlargest(50, 'Ár (USD)')

    # 4. Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő sorrendbe!
    top50_df = top50_df.sort_values(by='24h Árfolyamváltozás (%)', ascending=False)

    # 5. Hozz létre egy új oszlopot a top50_df-be change_direction néven
    def change_direction(value):
        if value > 0:
            return "+"
        elif value < 0:
            return "-"
        else:
            return "0"

    top50_df['Változás iránya'] = top50_df['24h Árfolyamváltozás (%)'].apply(change_direction)

    # Az új DataFrame kiírása
    print("\nTop 50 kriptovaluta:")
    print(top50_df[['Név', 'Szimbólum', 'Ár (USD)', 'Piaci kapitálizáció', '24h Árfolyamváltozás (%)', 'Változás iránya']])

else:
    print("Hiba történt az API hívás során:", response.status_code)
