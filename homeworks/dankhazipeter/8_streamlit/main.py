import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_KEY = st.secrets["api"]["key"]


@st.cache_data
def get_current_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={
        city}&appid={API_KEY}&units=metric"
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return response.json()
    return None


@st.cache_data
def get_weather_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={
        city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


st.title("Weather App")
city = st.sidebar.text_input("Enter city name", "London")

if city:
    # Fetch current weather
    weather = get_current_weather(city)
    if weather:
        st.subheader(f"Current Weather in {city}")
        temp = weather['main']['temp']
        humidity = weather['main']['humidity']
        wind_speed = weather['wind']['speed']

        col1, col2, col3 = st.columns(3)
        col1.metric("Temperature", f"{temp} °C")
        col2.metric("Humidity", f"{humidity} %")
        col3.metric("Wind Speed", f"{wind_speed} m/s")

        # Display map
        st.map(pd.DataFrame(
            [[weather['coord']['lat'], weather['coord']['lon']]], columns=['lat', 'lon']))
    else:
        st.warning("City not found or API error occurred!")

    # Fetch forecast data
    forecast = get_weather_forecast(city)
    if forecast:
        st.subheader(f"Temperature Forecast for {city} (next 5 days)")
        forecast_data = []
        for item in forecast['list']:
            forecast_data.append({
                "datetime": item["dt_txt"],
                "temperature": item["main"]["temp"]
            })
        df = pd.DataFrame(forecast_data)
        df["datetime"] = pd.to_datetime(df["datetime"])

        # Plotly line chart
        fig = px.line(df, x="datetime", y="temperature")
        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Temperature (°C)",
        )
        st.plotly_chart(fig)
    else:
        st.warning("Forecast data not available.")
