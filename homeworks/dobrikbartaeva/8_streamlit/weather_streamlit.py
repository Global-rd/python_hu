import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import datetime


API_KEY = st.secrets["weather"]["api_key"]
BASE_URL = "http://api.openweathermap.org/data/2.5/"

#ez a weatheres, de kell egy forecastos is... 
def fetch_data(city, params):
    print(f"Fetch {params} data for {city}")
    url = f"{BASE_URL}{params}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch {endpoint} data: {response.status_code} - {response.text}")
        return None

st.title("Robot Dreams Python - Weather Map & Data Visualization App")

city = st.text_input("Enter city name", "London")

data_weather = fetch_data(city,"weather")
data_forecast = fetch_data(city,"forecast")

def current_weather():
    if data_weather:
        st.header(f"Current Weather in {city}")
        temp = data_weather['main']['temp']
        humidity = data_weather['main']['humidity']
        wind_speed = data_weather['wind']['speed']
        col1, col2, col3 = st.columns(3)

        with col1: st.metric(label="Temperature (°C)", value=temp)
        with col2: st.metric(label="Humidity (%)", value=humidity)
        with col3: st.metric(label="Wind Speed (m/s)", value=wind_speed)
        
        #map:
        lat = data_weather['coord']['lat']
        lon = data_weather['coord']['lon']
        st.map(pd.DataFrame([[lat, lon]], columns=['lat', 'lon']))
    else:
        st.error("No data available. Check the city name.")

 
if __name__ == "__main__":
    current_weather()
