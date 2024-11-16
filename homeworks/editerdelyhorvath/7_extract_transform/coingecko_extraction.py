'''

7. Házi Feladat

CoinGeckoAPI class a 7. házifeladat adatelemzéséhez

Adatok kinyerése a CoinGecko public API-járól. 
A kövekező endpoint-ról 
“https://api.coingecko.com/api/v3/coins/markets”  húzd le 
a 250 legnagyobb market cap-pel rendelkező kriptovalutát
1 api hívással 
ahol a *market cap = kibocsátott darabszám * ár
Dokumentáció: https://docs.coingecko.com/reference/coins-markets

'''

import requests

class CoinGeckoAPI:
    """Class to interact with the CoinGecko API"""

    def __init__(self, vs_currency="usd", order="market_cap_desc", per_page=250, page=1):
        self.url = "https://api.coingecko.com/api/v3/coins/markets"
        self.params = {
        "vs_currency": vs_currency,
        "order": order,
        "per_page": per_page,
        "page": page
        }
        
    def fetch_data(self):
        """Fetch data from the CoinGecko API"""
        try:
            response = requests.get(url=self.url, params=self.params)
            if response.status_code == 200:
                return response.json() # return json data
            else:
                print(f"API call failed with {response.status_code} status code.")
                return None
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}.")
            return None
