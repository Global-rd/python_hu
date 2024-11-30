"""
Author: Gaál István Tamás
Task: Homework-8
"""
import requests
import pandas as pd
import streamlit as st
import plotly.express as px

API_KEY = st.secrets["openweathermap"]["api_key"]
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL= "http://api.openweathermap.org/data/2.5/forecast"

#fetch data
@st.cache_data(ttl=3600)
def fetchweather_and_forecast_data(city,url):
    params = {'appid': API_KEY,
                "q" : city,
                "units" : "metric"}
    
    response = requests.get(f"{url}", params=params)
   
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f" Failed to fetch data: {response.status_code} - {response.text}")
        return None

st.title("Robot Dreams Python - Weather Map & Data Visualization App")
st.caption("Enter city name")

city = st.text_input(label_visibility = 'collapsed',label= "city name", value= "London")

weather_data = fetchweather_and_forecast_data(city, WEATHER_URL)

if city:
    st.subheader(f"Current Weather in {city}")
    kpi1, kpi2, kpi3 = st.columns(3)

    with kpi1:
        st.metric(label="Temperature (°C)", value= f"{weather_data["main"]["temp"]:.2f}°C")
    
    with kpi2:
        st.metric(label="Humidity (%)", value= f"{weather_data["main"]["humidity"]:.0f}%")

    with kpi3:
        st.metric(label="Wind Speed (m/s)", value= f"{weather_data["wind"]["speed"]:.2f}m/s")
    
    st.subheader("Weather Map")
    map_data = pd.DataFrame({'latitude': [weather_data["coord"]["lat"]], "longitude": [weather_data["coord"]["lon"]]})
    st.map(map_data)
else:
     st.error("No data available.")

#Forecast
forecast_data = fetchweather_and_forecast_data(city, FORECAST_URL)

st.subheader("Temperature Trends (Next 5 Days)")

if "list" in forecast_data:
    df = pd.DataFrame(forecast_data["list"])
    times = df["dt_txt"]
    temps = []
    for i in range(0, 40):
        temps.append(df["main"][i].get("temp"))

    temp_date_df = pd.DataFrame({"Time": times, "Temp": temps})
    fig_temp = px.line(temp_date_df,y = "Temp", x = "Time")
    st.plotly_chart(fig_temp)

else:
     st.error("No data available.")
