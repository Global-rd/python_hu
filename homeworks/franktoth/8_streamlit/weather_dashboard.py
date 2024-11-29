import streamlit as st
import pandas as pd
import requests
import time
import plotly.express as px

API_KEY = st.secrets["polygon"]["api_key"]
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

last_fetch = 0
cached_data = {}

def fetch_weather_data(city):
    global last_fetch, cached_data

    current_time = time.time()
    if city in cached_data and current_time - last_fetch < 300:
        return cached_data[city]

    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        cached_data[city] = data
        last_fetch = current_time
        return data
    except requests.exceptions.RequestException as e:
        return {"error": f"Error fetching data for {city}: {e}"}

def main():
    st.title("Weather App")
    city = st.sidebar.text_input("Enter city name", "Budapest")
    weather_data = fetch_weather_data(city)

    if "error" in weather_data:
        st.error(weather_data["error"])
    else:
        city_name = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        lat = weather_data["coord"]["lat"]
        lon = weather_data["coord"]["lon"]

        st.header(f"Weather in {city_name}")
        col1, col2, col3 = st.columns(3)
        col1.metric("Temperature", f"{temperature} °C")
        col2.metric("Humidity", f"{humidity}%")
        col3.metric("Wind Speed", f"{wind_speed} m/s")

        map_data = pd.DataFrame({"latitude": [lat], "longitude": [lon]})
        st.map(map_data)

if __name__ == "__main__":
    main()