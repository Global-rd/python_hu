'''
8. Házi Feladat

Weather app fejlesztése a feladat leírásban megadott módon.

'''


import streamlit as st
import pandas as pd
from datetime import datetime, timezone

from db_connector import SqliteDB 
from weather_app_functions import get_weather_data, process_forecast_data, log_search


# Set API
API_KEY = st.secrets["polygon"]["api_key"]
BASE_URL = "http://api.openweathermap.org/data/2.5/"

# Page config and Header
st.set_page_config(page_title="Weather App", layout="wide")
st.markdown("""
    <h1 style='text-align: center;'>
        Robot Dreams Python - Weather<br>
        Map & Data Visualization App
    </h1>
    """, unsafe_allow_html=True)

# Set City
with st.sidebar:
    st.header("Search City")
    city = st.text_input("Enter city name:", "Pestújhely")
    show_forecast = st.checkbox("Show forecast (Extra)")


st.subheader(f"Current Weather in {city}")



# create Weather_logs.db if not exists
with SqliteDB('weather_logs.db') as db:
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS searches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        temperature REAL,
        humidity REAL,
        wind_speed REAL,
        search_time TEXT
    )
    '''
    db.conn.execute(create_table_query)


# Get weather data
weather_data = get_weather_data('weather', city, API_KEY, BASE_URL)

if weather_data:
    # KPI 
    col1, col2, col3 = st.columns(3)

    col1.metric("Temperature (°C)", weather_data['main']['temp'])
    col2.metric("Humidity (%)", weather_data['main']['humidity'])
    col3.metric("Wind speed (m/s)", weather_data['wind']['speed'])

    # Map
    lat = weather_data['coord']['lat']
    lon = weather_data['coord']['lon']
    st.map(pd.DataFrame({'lat': [lat], 'lon': [lon]}))

    # Custom divider
    st.markdown("""
    <hr style='height:2px; border:none; color:#333; background-color:#333;' />
    """, unsafe_allow_html=True)


    # Extra: Weather forecast
    if show_forecast:
        forecast_data = get_weather_data('forecast', city, API_KEY, BASE_URL)
        if forecast_data:
            forecast_df = process_forecast_data(forecast_data)
            
            st.subheader(f"Temperature Trends in {city} (Next 5 Days)")

            # Simple forecast with line chart
            st.line_chart(forecast_df.set_index('Day_Time')['main'].apply(lambda x: x['temp']))


    # Extra task: Logging to SQLite using log_search from weather_app_functions.py

    log_search(
        city=city,
        temperature=weather_data['main']['temp'],
        humidity=weather_data['main']['humidity'],
        wind_speed=weather_data['wind']['speed'],
        db_name='weather_logs.db'  
    )

else:
    st.error("No data available. Check the City.")


