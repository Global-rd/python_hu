import streamlit as st
import requests
import pandas as pd


#[openweather]
#api_key = "aa0632045d988cd5591e0c7087742ad7"

api_key = st.secrets["openweather"]["api_key"]
# api_key = "aa0632045d988cd5591e0c7087742ad7"
city = "London"

@st.cache_data(ttl=14400) # 4 órás cache
def get_data(city, method): # method: weather, forecast

    url = f"http://api.openweathermap.org/data/2.5/{method}?q={city}&appid={api_key}&units=metric"
    response = requests.get(url=url)
    
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch data: {response.status_code} - {response.text}")
        return None
    
@st.cache_data(ttl=14400)   
def get_coordinates(city):
    coordinates = get_data(city=city, method="weather")["coord"]
    coordinates_df = pd.DataFrame([coordinates])
    return coordinates_df

@st.cache_data(ttl=14400)
def get_teperature(city):
    temperature = get_data(city=city, method="weather")["main"]["temp"]
    return temperature

@st.cache_data(ttl=14400)
def get_humidity(city):
    humidity = get_data(city=city, method="weather")["main"]["humidity"]
    return humidity

@st.cache_data(ttl=14400)
def get_wind_speed(city):
    wind_speed = get_data(city=city, method="weather")["wind"]["speed"]
    return wind_speed
