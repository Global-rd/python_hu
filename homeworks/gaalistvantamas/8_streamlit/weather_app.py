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

#Weather
@st.cache_data(ttl=3600) # 1 Hour
def fetch_weather_data(city):

    url = f"{WEATHER_URL}"

    params = {'appid': API_KEY,
                "q" : city,
                "units" : "metric"}
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f" Failed to fetch data: {response.status_code} - {response.text}")
        return None

st.title("Robot Dreams Python - Weather Map & Data Visualization App")
st.caption("Enter city name")

city = st.text_input(label_visibility = 'collapsed',label= "city name", value= "London")
data = fetch_weather_data(city)

if city:
    st.subheader(f"Current Weather in {city}")
    kpi1, kpi2, kpi3 = st.columns(3)

    with kpi1:
        st.metric(label="Temperature (°C)", value= f"{data["main"]["temp"]:.2f}°C")
    
    with kpi2:
        st.metric(label="Humidity (%)", value= f"{data["main"]["humidity"]:.0f}%")

    with kpi3:
        st.metric(label="Wind Speed (m/s)", value= f"{data["wind"]["speed"]:.2f}m/s")
    
    st.subheader("Weather Map")
    map_data = pd.DataFrame({'latitude': [data["coord"]["lat"]], "longitude": [data["coord"]["lon"]]})
    st.map(map_data)
else:
     st.error("No data available.")

#Forecast
st.subheader("Temperature Trends (Next 5 Days)")

@st.cache_data(ttl=10800) # 3 Hours
def fetch_forecast_weather_data(city):

    url = f"{FORECAST_URL}"

    params = {'appid': API_KEY,
                "q" : city,
                "units" : "metric"}
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f" Failed to fetch data: {response.status_code} - {response.text}")
        return None

forecast_data = fetch_forecast_weather_data(city)

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
