import streamlit as st
import pandas as pd
import requests
import sqlite3
import plotly.express as px
from datetime import datetime as dt, timedelta as td

API_KEY = st.secrets["polygon"]["api_key"]
BASE_URL = "https://api.openweathermap.org/data/2.5/"

#Cache the function for fetching weather data from the API
@st.cache_data(ttl=86400)
def fetch_weather_data(city, endpoint):

    url = f"{BASE_URL}{endpoint}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        st.warning(f"Failed to fetch data: {response.status_code} - {response.text}")
        return None

#Inicialize an SQLite database
def log_search(city, temp, humidity, wind_speed):
    conn = sqlite3.connect("homeworks/kirkovvalentiniván/8_streamlit/weather_log.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS searches
              (city TEXT, temperature REAL, humidity REAL, wind_speed REAL, timestamp TEXT)""")
    cursor.execute("INSERT INTO searches VALUES (?,?,?,?,?)",
              (city, temp, humidity, wind_speed, dt.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    query = "SELECT * FROM searches"
    log_data = pd.read_sql_query(query, conn)
    print(log_data)
    conn.close()

#Upload streamlit program
st.title("Robot Dreams Python - Weather Map & Data Visualization App")

#Creating the city name
city = st.text_input("Enter city name", "Budapest")

#Retrieve and proceed data 
if city:
    current_weather = fetch_weather_data(city, endpoint="weather")
    if current_weather:
        #Actual weather information
        temp = current_weather["main"]["temp"]
        humidity = current_weather["main"]["humidity"]
        wind_speed = current_weather["wind"]["speed"]
        
        #Display Key Metrics
        st.subheader(f"Current weather in {city}")
        col1, col2, col3 = st.columns(3)
        col1.metric("Temperature (°C)", f"{temp} °C")
        col2.metric("Humidity (%)", f"{humidity} %")
        col3.metric("Wind Speed (m/s)", f"{wind_speed} m/s")

        log_search(city, temp, humidity, wind_speed)
        print (log_search)

        #Display Map
        st.subheader("Weather Map")
        st.map(pd.DataFrame({"lat": [current_weather["coord"]["lat"]], "lon": [current_weather["coord"]["lon"]]}))

    else:
        st.error("Couldn't fetch weather data. Please check the city name and try again.")

    forecast_data = fetch_weather_data(city, endpoint="forecast")
    if forecast_data:
        forecast_list = forecast_data["list"]
        forecast_df = pd.DataFrame([{
            "datetime": item["dt_txt"],
            "temperature": item["main"]["temp"]
        } for item in forecast_list])

        #Filter for 12-hour intervals
        forecast_df["datetime"] = pd.to_datetime(forecast_df["datetime"])
        forecast_df = forecast_df[forecast_df["datetime"].dt.hour.isin([0, 12])]

        #Create the line chart
        fig = px.line(
            forecast_df,
            x="datetime",
            y="temperature",
            title = "Temperature Trend (Next 5 Days)",
            labels = {"datetime": "Datetime", "temperature": "Temperature (°C)"}
            )
        
        #Customize X-axis
        fig.update_layout(
            xaxis = dict(
                tickformat = "%d-%m %H:%M",
                tickmode = "auto",
                nticks = len(forecast_df)
            )
        )

        #Display the chart
        st.plotly_chart(fig)      
    else:
        st.error("Couldn't fetch weather data. Please check the city name and try again.")
