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
    if response.status_code == 200:
        return response.json()
    return None

    if not city: 
        st.warning("Which city?")
        s_main = pd.Series()
        s_wind = pd.Series()
        coord = {}
        return s_main, s_wind, coord
    
    elif response.status_code == 200:
        st.warning("We didn't find that city, try another one!")
        s_main = pd.Series()
        s_wind = pd.Series()
        coord = {}
        return s_main, s_wind, coord
    
    else:
        response_body = response.json()
        s_main = pd.Series(response_body["main"])
        s_wind = pd.Series(response_body["wind"])
        coord = response_body["coord"]
        return s_main, s_wind, coord
        
def display_weather_data(city, main, wind, coord):
    

st. title("Robot Dreams Weather Map & Visualizaton WebApp")
st.subheader
fetch_weather_data("Budapest")
