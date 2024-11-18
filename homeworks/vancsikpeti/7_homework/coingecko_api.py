import requests

class CoinGecko:

    def get_data(p_url_mode: str, p_vs_currency: str, p_limit: int):
        url = f"https://api.coingecko.com/api/v3/coins/{p_url_mode}"
        header = {"accept": "application/json"}
        param = {
            "vs_currency": p_vs_currency,
            "per_page": p_limit
            }
        data = requests.get(url, headers=header, params=param).json()
        return data

#city = response.get("name", "Unkown")
#print(city)
#temp = response["main"].get("temp", "N/A")
#print(temp)
#weather_desc = response["weather"][0].get("description", "No desc. available")
#print(weather_desc)