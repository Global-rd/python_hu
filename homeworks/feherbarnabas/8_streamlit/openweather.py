import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_KEY = st.secrets["openweather"]["api_key"]
ENDPOINT = "https://api.openweathermap.org/"
VERSION = "2.5"

@st.cache_data(ttl=86400)
def fetch_weather_data(city):
    weather_url = f"{ENDPOINT}data/{VERSION}/weather?q={city}&appid={API_KEY}&units=metric"
    print(f"Fetch weather data of {city}")
    response = requests.get(weather_url)