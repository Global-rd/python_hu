import streamlit as st
import requests
import pandas as pd

# API 
API_KEY = st.secrets["polygon"]["api_key"]

@st.cache_data(ttl=86400)
def get_weather_data(city_name):
    if not city_name:
        raise ValueError("City name cannot be empty.")

    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city_name, "appid": API_KEY, "units": "metric"}
    response = requests.get(url, params=params)

    try:
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to fetch weather data: {e}")

    return response.json()


st.set_page_config(page_title="City Weather", layout="wide")
st.title("Robot Dream Python - Weather Map & Data Visualization App")

with st.sidebar:
     city_name = st.text_input("Enter city name:", value="Budapest")

if not city_name:
    st.warning("Please enter a city name to continue!")

# OpenWeatherMap API call
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

try:
    data = get_weather_data(city_name)
    # Datas
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    lat, lon = data["coord"]["lat"], data["coord"]["lon"]

    # Key metrics 
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature (°C)", f"{temperature}°C")
    col2.metric("Humidity (%)", f"{humidity}%")
    col3.metric("Wind_speed (m/s)", f"{wind_speed} m/s")

    # Map
    st.subheader(f"{city_name} map:")
    city_map_data = pd.DataFrame({"lat": [lat], "lon": [lon]})
    st.map(city_map_data)

except requests.exceptions.RequestException as e:
    st.warning(f"An error occurred during the API call: {e}")
except KeyError:
    st.warning("An error occurred: Check that you entered the correct city name.")