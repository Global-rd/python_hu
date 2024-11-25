import streamlit as st
import pandas as pd
import requests
import plotly.express as px

API_KEY = st.secrets["weather"]["api_key"]
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

# fetching actual weather
@st.cache_data(ttl=7200)
def fetch_city_weather(city_name):
    url = f"{WEATHER_URL}?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Sorry, this city is not in the database, so no weather data found for. Try another city.")
        return None

# fetching weather forecast
@st.cache_data(ttl=7200)
def fetch_city_forecast(city_name):
    url = f"{FORECAST_URL}?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Sorry, this city is not in the database, so no weather forecast available.")
        return None

# processing actual weather data
def process_weather_data(data):
    try:
        return {
            "Temperature (°C)": round(data["main"]["temp"], 2),
            "Humidity (%)": data["main"]["humidity"],
            "Wind Speed (m/s)": round(data["wind"]["speed"], 2),
        }
    except KeyError as e:
        st.error(f"Data processing error: Missing key {e}")
        return None

# processing weather forecast data (convert into pandas DataFrame)
def process_forecast_data(data):
    try:
        df = pd.DataFrame(data["list"])
        df["datetime"] = pd.to_datetime(df["dt_txt"])
        df["Temperature (°C)"] = df["main"].apply(lambda x: x["temp"])
        return df
    except KeyError as e:
        st.error(f"Forecast processing error: Missing key {e}")
        return None

# predefined format for center alignment
def centered_markdown(content, font_size=18, tag="div"):
    st.markdown(
        f"""
        <{tag} style='text-align: center; font-size: {font_size}px; font-weight: bold;'>
            {content}
        </{tag}>
        """,
        unsafe_allow_html=True
    )

# predefined format for kpi
def display_kpi(icon, title, value, unit):
    st.markdown(
        f"""
        <div style='text-align: center;'>
            <h5>{icon} {title}</h5>
            <h2>{value} {unit}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

# current weather data display
def display_weather_data(weather_data):
    if weather_data:
        kpi1, kpi2, kpi3 = st.columns(3)
        with kpi1:
            display_kpi("🌡️", "Temperature (°C)", weather_data['Temperature (°C)'], "°C")
        with kpi2:
            display_kpi("💧", "Humidity (%)", weather_data['Humidity (%)'], "%")
        with kpi3:
            display_kpi("🌬️", "Wind Speed (m/s)", weather_data['Wind Speed (m/s)'], "m/s")

# displays the map with city"s geographical location
def create_map(data):
    try:
        map_data = pd.DataFrame({
            "latitude": [data["coord"]["lat"]],
            "longitude": [data["coord"]["lon"]]
        })
        st.map(map_data)
    except KeyError as e:
        st.error(f"Map generation error: Missing key {e}")

# display text on page header
centered_markdown ("Robot Dreams Python", font_size=32)
centered_markdown ("Weather Map & Data Visualiziaton App", font_size=24)
st.divider()
centered_markdown ("Enter a city name:", font_size=18)

# input city name
city_name = st.text_input(" ", "London")

# actual city on map
if city_name:
    data = fetch_city_weather(city_name)
    if data:
        weather_data = process_weather_data(data)
        if weather_data:
            display_weather_data(weather_data)
            st.divider()
            centered_markdown ("City Location on Map", font_size=18)
            create_map(data)

# temperature trends graph 5days_3hrs
forecast_data = fetch_city_forecast(city_name)
if forecast_data:
    df = process_forecast_data(forecast_data)
    if df is not None:      
        st.divider()
        centered_markdown ("Temperature Trends (Next 5 days - 3-hour intervals)", font_size=18)
        fig = px.line(
            df,
            x="datetime",
            y="Temperature (°C)",
            labels={"datetime": "Date & Time", "Temperature (°C)": "Temperature (°C)"},
        )
        st.plotly_chart(fig, use_container_width=True)