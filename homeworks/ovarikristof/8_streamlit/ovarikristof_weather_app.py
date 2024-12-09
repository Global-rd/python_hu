import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# API-kulcs betöltése a secrets fájlból
API_KEY = st.secrets["polygon"]["api_key"]
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"

# Cache-elt függvény az aktuális időjárás lekérdezéséhez
@st.cache_data(ttl=86400)
def get_current_weather(city, api_key):
    url = f"{BASE_URL}?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Cache-elt függvény az 5 napos előrejelzés lekérdezéséhez
@st.cache_data(ttl=86400)
def get_weather_forecast(city, api_key):
    url = f"{FORECAST_URL}?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Sidebar: városnév bekérése
st.sidebar.title("Weather App")
city = st.sidebar.text_input("Enter a city:", "Budapest")

# API hívás az aktuális időjárási adatok lekérdezésére
weather_data = get_current_weather(city, API_KEY)

# Hibaüzenet vagy időjárási adatok megjelenítése
if weather_data is None:
    st.warning("Failed to retrieve weather data. Check the city name!")
else:
    # Adatok kinyerése az API válaszából
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    lat = weather_data['coord']['lat']
    lon = weather_data['coord']['lon']

    # Oldal címe
    st.title(f"Weather in {city}")

    # Key metrics megjelenítése
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature °C", f"{temp} °C")
    col2.metric("Humidity %", f"{humidity} %")
    col3.metric("Wind speed m/s", f"{wind_speed} m/s")

    # Térkép megjelenítése
    st.map(pd.DataFrame({'lat': [lat], 'lon': [lon]}))

    # 5 napos előrejelzés lekérése
    st.header("Temperature trend for the next 5 days")
    forecast_data = get_weather_forecast(city, API_KEY)

    if forecast_data is not None:
        # Feldolgozzuk az előrejelzési adatokat
        forecast_list = forecast_data['list']
        forecast_df = pd.DataFrame({
            "Datetime": [item["dt_txt"] for item in forecast_list],
            "Temperature (°C)": [item["main"]["temp"] for item in forecast_list]
        })

        # Konvertáljuk a "Datetime" oszlopot dátum-idő formátumba
        forecast_df["Datetime"] = pd.to_datetime(forecast_df["Datetime"])

        # Plot készítése Plotly-val
        fig = px.line(
            forecast_df,
            x="Datetime",
            y="Temperature (°C)",
            title=f"{city}'s temperature trend for the next 5 days",
            #labels={"Temperature (°C)": "Temperature (°C)"},
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Failed to load forecast data.")


#https://ovarikristofweather.streamlit.app