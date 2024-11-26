import streamlit as st
import pandas as pd
import requests
import plotly.express as px

API_KEY = st.secrets["polygon"]["api_key"]
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather_data(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "lat": data["coord"]["lat"],
            "lon": data["coord"]["lon"],
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Error fetching data for {city}: {e}"}

def main():
  st.title("Weather App")
  city = st.sidebar.text_input("Enter City Name")
  weather_data = fetch_weather_data(city)

  if "error" in weather_data:
    st.error(weather_data["error"])
  else:
    city_name = weather_data["city"]
    temperature = weather_data["temp"]
    humidity = weather_data["humidity"]
    wind_speed = weather_data["wind_speed"]
    lat = weather_data["lat"]
    lon = weather_data["lon"]

    st.header(f"Weather in {city_name}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", f"{temperature} °C")
    col2.metric("Humidity", f"{humidity}%")
    col3.metric("Wind Speed", f"{wind_speed} m/s")

    st.map(latitude=lat, longitude=lon, zoom=11)

if __name__ == "__main__":
  main()