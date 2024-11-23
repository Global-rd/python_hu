import requests
import settings as s

url = "https://api.openweathermap.org/data/2.5/weather"
params = {"lat": s.BUDAPEST.get("lat", 0),
          "lon": s.BUDAPEST.get("lon", 0),
          "appid": s.OPENWEATHERMAP_API_KEY,
          "units": "metric"}


response = requests.get(url=url, params=params).json()
print(response)

city = response.get("name", "Unkown")
print(city)
temp = response["main"].get("temp", "N/A")
print(temp)
weather_desc = response["weather"][0].get("description", "No desc. available")
print(weather_desc)