#Homework - Nagy Norbert
import requests

class InvalidDataPerPageReached(Exception):
    """Data per page param in request has to be between 1 and 250.
       More information here:
       https://docs.coingecko.com/reference/coins-markets"""
    pass

url = "https://api.coingecko.com/api/v3/coins/markets"
headers = {"accept": "application/json"}
params = {"vs_currency":"eur",
          "order":"market_cap_desc"}

def get_coins_data(data_per_page:int):
    params.update({"per_page":data_per_page})
    if data_per_page > 250 or data_per_page < 1:
        raise InvalidDataPerPageReached("Number of data per page is invalid.")
    response = requests.get(url=url,params=params,headers=headers).json()
    return response