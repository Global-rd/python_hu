import streamlit as st
import pandas as pd
from pandas import DataFrame
import numpy as np
import datetime
import requests
from requests import Response


class FetchWeatherResult:
    def __init__(self):
        self.status_code: int
        self.dataFrame: DataFrame
        self.lon: float
        self.lat: float
        self.temperature: str
        self.humidity: str
        self.wind_speed: str
        self.no_data_found: bool
        self.error_text: str
        self.response: Response


API_KEY = st.secrets["openweather"]["api_key"]


# @st.cache_data(ttl=86400)
def fetch_weather_data(city) -> FetchWeatherResult:

    result = FetchWeatherResult()

    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={
        city}&appid={API_KEY}&units=metric'

    response = requests.get(url=weather_url)

    if response.status_code == 200:
        result.response = response
    elif response.status_code == 404:
        result.response = response
        result.status_code = 404
        result.error_text = 'Not data found for the selected city'
    else:
        result.response = response
        result.status_code = response.status_code
        result.error_text = response.text
    return result


def process_weather_data(weather_result: FetchWeatherResult) -> FetchWeatherResult:

    weather_data = weather_result.response.json()
    fetchData = weather_result
    try:
        main_section = weather_data['main']
        coord_section = weather_data['coord']
        wind_section = weather_data['wind']
    except:
        print(f'No data found')
        fetchData.no_data_found = True

    if 'main' in weather_data:
        df = pd.DataFrame([main_section])
        print(df)
        fetchData.humidity = df.at[0, 'humidity']
        fetchData.temperature = df.at[0, 'temp']
        fetchData.no_data_found = False
    if 'coord' in weather_data:
        df = pd.DataFrame([coord_section])
        print(df)
        fetchData.lon = df.at[0, 'lon']
        fetchData.lat = df.at[0, 'lat']
    if 'wind' in weather_data:
        df = pd.DataFrame([wind_section])
        fetchData.wind_speed = df.at[0, 'speed']
        print(df)
    else:
        fetchData.no_data_found = True

    return fetchData


# """
# Page 'render'
# """


header = st.header(
    body=f"Robot Dreams Pyton - Weather Map & Data Visualization App")
text_input_city = st.text_input(label=f"Enter city name:", value="London")
fetch_button = st.button(label="Fetch")
kpi1, kpi2, kpi3 = st.columns(3)

# """
# Page 'interactions'
# """


if text_input_city:
    result = process_weather_data(fetch_weather_data(text_input_city))
    if result.no_data_found or result == None:
        st.error(f'No data found for the selected city: {text_input_city}')

    if result.no_data_found == False:
        sub_header = st.subheader(
            body=f'Current weather in:  {text_input_city}')
        df = pd.DataFrame({'lon': result.lon, 'lat': result.lat}, index=[0])
        kpi1.metric('Temperature (\u00B0C)', value=f'{
                    result.temperature} \u00B0C')
        kpi2.metric('Humidity (%)', value=f'{result.humidity} %')
        kpi3.metric('Wind Speed (m/s)', value=f'{result.wind_speed} m/s')
        city_map = st.map(data=df, latitude="lat", longitude="lon")
