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
    
    if not city: 
        print("Which city?")
        return None
    
    elif response.status_code == 200:
        return response.json()
    
    else:
        st.warning(f"Didn't manage to fetch data ({response.status_code}). Try another one!")
        return None
    
st.sidebar.title("Weather Data")
city = st.sidebar.text_input("City name:", placeholder="Type a city...")

if city:
    data = fetch_weather_data(city)

    if data:
        
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        coords = data["coord"]

        st.title(f"Weather in {city.capitalize()}:")
        st.metric(label="Temperature (°C)", value=f"{temp}°C")
        st.metric(label="Humidity (%)", value=f"{humidity}%")
        st.metric(label="Wind speed (m/s)", value=f"{wind_speed} m/s")

        st.subheader("Map")
        map_data = pd.DataFrame([{"lat": coords["lat"], "lon": coords["lon"]}])
        st.map(map_data)
    else:
        st.warning("There is no arriving data...")
else:
    st.info("Search up a city in the sidebar!")