#Homework - Nagy Norbert
import requests
import streamlit as st
import pandas as pd

API_KEY = st.secrets["openweathermap"]["API_KEY"]
ENDPOINT = "http://api.openweathermap.org/"
VERSION = "2.5"

@st.cache_data(ttl=86400)
def fetch_actual_weather_data(city):
    weather_url = f"{ENDPOINT}data/{VERSION}/weather?q={city}&appid={API_KEY}&units=metric"
    print(f"Fetch actual weathor of {city}")
    response = requests.get(weather_url)
    if not city:
        st.warning("City name is empty!")
        s_main = pd.Series()
        s_wind = pd.Series()
        coord = {}
        return s_main,s_wind,coord
    elif response.status_code != 200:
        st.warning("Data fetch is unsuccess. City name may be incorrect!")
        s_main = pd.Series()
        s_wind = pd.Series()
        coord = {}
        return s_main,s_wind,coord
    else:
        resp_body = response.json() 
        s_main = pd.Series(resp_body["main"])
        s_wind = pd.Series(resp_body["wind"])
        coord = resp_body["coord"]
        return s_main,s_wind,coord

def show_current_weather_data(city,main,wind,coord):
    st.subheader(f"Current Weather in {city.capitalize()}")
    df = pd.DataFrame(
        [
            {"Temperature (°C)": f"{main["temp"]:.2f} °C", "Humidity": f"{main["humidity"]:.2f} %", "Wind speed (m/s)": f"{wind["speed"]:.2f} m/s"}
        ]
    )
    st.dataframe(df,hide_index=True)
    st.subheader("Weather Map")
    df_map = pd.DataFrame({
        'latitude': [coord["lat"]],
        'longitude': [coord["lon"]]
    })
    st.map(df_map,zoom=12)
    
st.title("Robot Dreams Python - Weather Map & Data Visualization App")
city = st.text_input("Enter city name").strip()
weather_main,weather_wind,coord = fetch_actual_weather_data(city)
if not (weather_main.empty or weather_wind.empty) and coord:
    show_current_weather_data(city,weather_main,weather_wind,coord)