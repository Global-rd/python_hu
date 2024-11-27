import streamlit as st
import pandas as pd
import requests
from geopy.geocoders import Nominatim

API_KEY = st.secrets["openweather"]["api_key"]
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

@st.cache_data(ttl=86400)
def fetch_city_info(city):
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch data: {response.status_code} - {response.text}")
        return None

def get_lat_lon(city_name):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city_name)
    return location.latitude, location.longitude

st.title("Current Weather Dashboard")
st.sidebar.header("City selection")

city_name = st.sidebar.text_input("Enter a city name (e.g.: Prague, New York, Cairo)", "London")

data = fetch_city_info(city_name)

def process_data(data):
    if data:
        df = pd.DataFrame([{
            "Temperature": data["main"]["temp"],
            "Humidity": data["main"]["humidity"],
            "Wind speed": data["wind"]["speed"]
        }])
        return df
    else:
        st.error("No valid city name!")
        return None

if data:
    df = process_data(data)
    st.header(f"Weather details now: {city_name.upper()}")

    if df is not None:
        kpi1, kpi2, kpi3 = st.columns(3)
        with kpi1:
            st.metric(label="Temperature (℃)", value=f"{df['Temperature'][0]:.2f}℃")
        with kpi2:
            st.metric(label="Humidity (%)", value=f"{df['Humidity'][0]:.2f}%")
        with kpi3:
            st.metric(label="Wind speed (m/s)", value=f"{df['Wind speed'][0]:.2f} m/s")

        # Get latitude and longitude
        latitude, longitude = get_lat_lon(city_name)

        # Create a dataframe with the coordinates
        map_df = pd.DataFrame({
            'lat': [latitude],
            'lon': [longitude]
        })

        # Display the map
        st.map(map_df)
else:
    st.error("No data available. Check the city name.")


