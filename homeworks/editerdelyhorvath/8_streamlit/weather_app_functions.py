'''

Weather_app.py hoz használt funkciók 

'''

import streamlit as st
import requests
import pandas as pd
from datetime import datetime, timezone
from db_connector import SqliteDB

@st.cache_data(ttl=600) # TTL (Time To Live) 10 min
def get_current_weather(city, api_key, base_url):
    """
    Fetches the current weather data for a given city.
    
    :param city: str, name of the city
    :param api_key: str, OpenWeatherMap API key
    :param base_url: str, base URL for the API
    :return: dict or None
    """
    url = f"{base_url}weather?q={city}&appid={api_key}&units=metric&lang=hu"
    response = requests.get(url)
    if response.status_code != 200:
        st.warning(f"Failed to fetch data: {response.status_code} - {response.text}")
        return None
    data = response.json()
    return data

@st.cache_data(ttl=600) # TTL (Time To Live) 10 min
def get_forecast(city, api_key, base_url):
    """
    Fetches the weather forecast data for a given city.
    
    :param city: str, name of the city
    :param api_key: str, OpenWeatherMap API key
    :param base_url: str, base URL for the API
    :return: dict or None
    """
    url = f"{base_url}forecast?q={city}&appid={api_key}&units=metric&lang=hu"
    response = requests.get(url)
    if response.status_code != 200:
        st.warning(f"Failed to fetch data: {response.status_code} - {response.text}")
        return None
    data = response.json()
    return data

def process_forecast_data(forecast_data):
    """
    Processes the forecast data to prepare it for visualization.
    
    :param forecast_data: dict, forecast data from API
    :return: pandas.DataFrame
    """
    forecast_df = pd.DataFrame(forecast_data['list'])
    # Tz-aware objektum UTC-val
    forecast_df['dt_txt'] = pd.to_datetime(forecast_df['dt_txt']).dt.tz_localize('UTC')
    forecast_df = forecast_df[['dt_txt', 'main', 'weather', 'wind']]

    # Aktuális időpont UTC-ben
    current_time = datetime.now(timezone.utc)

    # Szűrés az aktuális időpont után
    forecast_df = forecast_df[forecast_df['dt_txt'] >= current_time]

    # Rendezés növekvő sorrendbe
    forecast_df = forecast_df.sort_values('dt_txt')

    # Csak a következő 40 adatpontot vesszük (5 nap * 8 adatpont/nap)
    forecast_df = forecast_df.head(40)

    # Új oszlop a dátum és idő formázásához
    forecast_df['Day_Time'] = forecast_df['dt_txt'].dt.strftime('%Y.%m.%d. %H:%M')  # Pl. "2024.11.24. 23:00"

    return forecast_df

def log_search(city, temperature, humidity, wind_speed, db_name='weather_logs.db'):
    """
    Logs the search parameters into the SQLite database.
    
    :param city: str, name of the city
    :param temperature: float, temperature in °C
    :param humidity: int, humidity percentage
    :param wind_speed: float, wind speed in m/s
    :param db_name: str, name of the SQLite database file
    """
    record = {
        'city': city,
        'temperature': temperature,
        'humidity': humidity,
        'wind_speed': wind_speed,
        'search_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    with SqliteDB(db_name) as db:
        db.write_single_record('searches', record)
