import requests
import streamlit as st
import json

@st.cache_data(ttl=86400) 
def fetch_weather(city: str):
    """
    Fetch weather data for a given city using the OpenWeather API.
    The result is cached for 24 hours (86400 seconds).
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





