import streamlit as st
import requests
import pandas as pd

api_key = st.secrets["openweather"]["api_key"]
city = "London"

@st.cache_data(ttl=14400) # 4 órás cache
def get_data(city, method): # method: weather, forecast

    url = f"http://api.openweathermap.org/data/2.5/{method}?q={city}&appid={api_key}&units=metric"
    response = requests.get(url=url)
    
    if response.status_code == 200:
        #weather = response.json()
        #forecast = response.json()
        #return weather, forecast
        data = response.json()
        return data
    else:
        st.error(f"Failed to fetch data: {response.status_code} - {response.text}")
        return None
    
weather = get_data(city, "weather")
forecast = get_data(city, "forecast")     

#@st.cache_data(ttl=14400)
def get_coordinates(data):
    coordinates = data["coord"]
    coordinates_df = pd.DataFrame([coordinates])
    return coordinates_df

#@st.cache_data(ttl=14400)
def get_teperature(data):
    temperature = data["main"]["temp"]
    return temperature

#@st.cache_data(ttl=14400)
def get_humidity(data):
    humidity = data["main"]["humidity"]
    return humidity

#@st.cache_data(ttl=14400)
def get_wind_speed(data):
    wind_speed = data["wind"]["speed"]
    return wind_speed

