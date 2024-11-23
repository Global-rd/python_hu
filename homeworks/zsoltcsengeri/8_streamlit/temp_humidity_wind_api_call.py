import requests
import streamlit as st

def fetch_weather(city: str):
    """
    Fetch weather data for a given city using the OpenWeather API.
    """
    API_KEY = st.secrets["openweather"]["api_key"]
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "units": "metric",
        "appid": API_KEY,
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

# Ensure this code only runs when the file is executed directly
if __name__ == "__main__":
    data = fetch_weather("London")
    print(data)
