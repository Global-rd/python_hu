import requests

class CoinGecko:

    def get_data(limit: int):
        url = "https://api.coingecko.com/api/v3/coins/markets"
        header = {"accept": "application/json"}
        param = {
            "vs_currency": "usd",
            "per_page": limit
            }
        data = requests.get(url, headers=header, params=param).json()
        return data

#city = response.get("name", "Unkown")
#print(city)
#temp = response["main"].get("temp", "N/A")
#print(temp)
#weather_desc = response["weather"][0].get("description", "No desc. available")
#print(weather_desc)