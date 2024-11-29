import streamlit as st
import requests
import plotly.express as px
import datetime
import pandas as pd


API_KEY = st.secrets["openweather"]["api_key"]


@st.cache_data (ttl=86400)
def get_weather_data(city: str, endpoint: str) -> dict:

    url = f'http://api.openweathermap.org/data/2.5/{endpoint}?q={city}&appid={API_KEY}&units=metric'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data from OpenWeather API: {e}")
        return {}


st.set_page_config(page_title="Weather Dashboard", layout="wide")

st.title("Robot Dreams Python - Weather Map & Data Visualization App")
city = st.text_input("Enter city name:", "Budapest").capitalize()
try:
    # Jelenlegi időjárás adatok
    st.subheader(f"Current Weather in {city}")
    current_weather = get_weather_data(city, "weather")
    forecast = get_weather_data(city, "forecast")

    # KPI
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Temperature (°C)", current_weather["main"]["temp"])
    with col2:
        st.metric("Humidity (%)", current_weather["main"]["humidity"])
    with col3:
        st.metric("Wind speed (m/s)", current_weather["wind"]["speed"])

    # Térkép
    lat = current_weather["coord"]["lat"]
    lon = current_weather["coord"]["lon"]

    city_location = pd.DataFrame({
        'latitude': [lat],
        'longitude': [lon]
    })

    st.subheader(f"Weather Map in {city}")
    st.map(city_location)


    # Előrejelzés adatok
    forecast_data = {
        "Date": [datetime.datetime.fromtimestamp(item["dt"]) for item in forecast["list"]],
        "Temperature(°C)": [item["main"]["temp"] for item in forecast["list"]],
        "Humidity (%)": [item["main"]["humidity"] for item in forecast["list"]]
    }

    # Hőmérséklet
    st.subheader(f"Temperature Trends (Next 5 Day) in {city}")
    fig_temp = px.line(
        x=forecast_data["Date"],
        y=forecast_data["Temperature(°C)"],
        labels={"x": "Date", "y": "Temperature (°C)"},
    )
    st.plotly_chart(fig_temp, use_container_width=True)

    # Páratartalom
    st.subheader(f"Humidity Trends (Next 5 Day) in {city}")
    fig_humidity = px.line(
        x=forecast_data["Date"],
        y=forecast_data["Humidity (%)"],
        labels={"x": "Date", "y": "Humidity (%)"},
    )
    st.plotly_chart(fig_humidity, use_container_width=True)

except requests.exceptions.RequestException as e:
    st.error(f"An error occurred while retrieving data: {e}")