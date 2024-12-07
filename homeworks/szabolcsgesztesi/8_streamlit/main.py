import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# API kulcs beállítása
API_KEY = st.secrets["openweathermap"]["api_key"]

# Adat lekérő függvény (cache-elve, TTL beállítással)
@st.cache_data(ttl=600)  # 10 percig él a cache
def get_data(endpoint, city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/{endpoint}?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Előrejelzési adatok feldolgozása
def process_forecast_data(forecast_data):
    df = pd.DataFrame(forecast_data["list"])
    df["datetime"] = pd.to_datetime(df["dt"], unit="s")
    df["temperature"] = df["main"].apply(lambda x: x["temp"])
    df["humidity"] = df["main"].apply(lambda x: x["humidity"])
    return df[["datetime", "temperature", "humidity"]]

# Plotly hőmérsékleti diagram
def plot_temperature_chart(df):
    fig = px.line(
        df,
        x="datetime",
        y="temperature",
        title="Temperature Forecast",
        labels={"datetime": "Date/Time", "temperature": "Temperature (°C)"},
        markers=True,
    )
    return fig

# Streamlit alkalmazás felépítése
st.title("Weather Dashboard 🌤️")

city = st.text_input("Enter a city", "Budapest")

if city:
    # Jelenlegi időjárás lekérése és megjelenítése
    current_weather = get_data("weather", city, API_KEY)
    if current_weather:
        st.subheader(f"Current Weather in {city}")
        
        # Három oszlop használata a KPI-ok megjelenítéséhez
        col1, col2, col3 = st.columns(3)
        col1.metric("Temperature", f"{current_weather['main']['temp']} °C")
        col2.metric("Humidity", f"{current_weather['main']['humidity']} %")
        col3.metric("Wind Speed", f"{current_weather['wind']['speed']} m/s")
        
        # Térkép megjelenítése
        lat = current_weather["coord"]["lat"]
        lon = current_weather["coord"]["lon"]
        st.map(pd.DataFrame({"lat": [lat], "lon": [lon]}))
    else:
        st.warning("Failed to fetch current weather data. Please check the city name.")

    # Előrejelzés lekérése és grafikon megjelenítése
    forecast_data = get_data("forecast", city, API_KEY)
    if forecast_data:
        st.subheader(f"5-Day Temperature Forecast for {city}")
        forecast_df = process_forecast_data(forecast_data)
        fig = plot_temperature_chart(forecast_df)
        st.plotly_chart(fig)
    else:
        st.warning("Failed to fetch forecast data. Please check the city name.")