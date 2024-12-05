import requests
import streamlit as st

@st.cache_data
def fetch_data(city, api_key, endpoint):
    """
    Általános API-hívás az OpenWeatherMap szolgáltatáshoz.
    Paraméterek:
        city (str): Város neve
        api_key (str): API kulcs
        endpoint (str): Az API végpontja ('weather' vagy 'forecast')
    Visszatérési érték:
        dict: Az API válasz JSON formátumban, vagy None, ha hiba történt.
    """
    url = f"http://api.openweathermap.org/data/2.5/{endpoint}?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
