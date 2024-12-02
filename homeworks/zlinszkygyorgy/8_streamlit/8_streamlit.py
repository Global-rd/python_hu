import streamlit as st
import pandas as pd
import requests

API_KEY = st.secrets["openweathermap"]["api_key"]

@st.cache_data(ttl=600)
def get_current_weather(city):
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.warning(f"Error fetching data: {response.status_code}")
        return None

def show_current_weather():
    st.title("Weather Dashboard")
    
    city = st.sidebar.text_input("Enter city name", "Budapest")
    
    current_weather = get_current_weather(city)
    
    if current_weather:
        st.header(f"Current Weather in {city}")
        temp = current_weather['main']['temp']
        humidity = current_weather['main']['humidity']
        wind_speed = current_weather['wind']['speed']
        col1, col2, col3 = st.columns(3)
        with col1: st.metric(label="Temperature (°C)", value=temp)
        with col2: st.metric(label="Humidity (%)", value=humidity)
        with col3: st.metric(label="Wind Speed (m/s)", value=wind_speed)
        
        lat = current_weather['coord']['lat']
        lon = current_weather['coord']['lon']
        st.map(pd.DataFrame([[lat, lon]], columns=['lat', 'lon']))
    else:
        st.error("No data available. Check the city name.")

if __name__ == "__main__":
    show_current_weather()