import sqlite3
from datetime import datetime
import requests
import pandas as pd
import streamlit as st
import plotly.express as px

# API Key from Streamlit secrets
API_KEY = st.secrets["api"]["key"]

# SQLite adatbázis inicializálása
conn = sqlite3.connect("weather_logs.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        temperature REAL,
        humidity INTEGER,
        wind_speed REAL,
        timestamp TEXT
    )
""")
conn.commit()


@st.cache_data(ttl=600)
def get_current_weather(city):
    """Fetch current weather from the API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={
        city}&appid={API_KEY}&units=metric"
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return response.json()
    return None


@st.cache_data(ttl=600)
def get_weather_forecast(city):
    """Fetch weather forecast from the API."""
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={
        city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def log_weather_data(city, temperature, humidity, wind_speed):
    """Log weather data into the SQLite database."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO logs (city, temperature, humidity, wind_speed, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (city, temperature, humidity, wind_speed, timestamp))
    conn.commit()


def show_logs():
    """Display recent search logs."""
    st.write("Below are the recent search logs:")
    cursor.execute(
        "SELECT city, temperature, humidity, wind_speed, timestamp FROM logs ORDER BY id DESC LIMIT 10")
    logs = cursor.fetchall()
    if logs:
        st.table(pd.DataFrame(logs, columns=[
            "City", "Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)", "Timestamp"]))
    else:
        st.write("No logs available.")


# Streamlit sidebar and main app
city = st.sidebar.text_input("Enter city name", "Balatonszepezd")

fetch_button = search_button = False

if st.sidebar.button("Fetch Weather for Entered City"):
    fetch_button = True
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

            # Log the data into SQLite
            log_weather_data(city, temp, humidity, wind_speed)

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
    else:
        st.warning("Please enter a city name!")

if st.sidebar.button("Show Search Logs"):
    search_button = True
    show_logs()

if not fetch_button and not search_button:
    st.title("Weather Forecast Application")
    st.write("Please enter a city name in the input box on the left and press the button to get current weather data and forecast.")
