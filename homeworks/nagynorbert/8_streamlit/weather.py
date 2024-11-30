#Homework - Nagy Norbert
import requests
import streamlit as st
import pandas as pd

API_KEY = st.secrets["openweathermap"]["API_KEY"]
ENDPOINT = "http://api.openweathermap.org/"
VERSION = "2.5"
WEATHER_URL = f"{ENDPOINT}/data/{VERSION}/weather"

params = {
    "appid": API_KEY,
    "units": "metric"
}

@st.cache_data(ttl=86400)
def fetch_actual_weather_data(city):
    params.update({"q":city})
    print(f"Fetch actual weathor of {city}")
    response = requests.get(url=WEATHER_URL,params=params)
    print(response.json())
    s_main, s_wind, coord = pd.Series(), pd.Series(), {}
    if not city:
        st.warning("City name is empty!")
    elif response.status_code != 200:
        st.warning("Data fetch was unsuccessful. City name may be incorrect!")
    else:
        resp_body = response.json()
        s_main = pd.Series(resp_body.get("main", {}))
        s_wind = pd.Series(resp_body.get("wind", {}))
        coord = resp_body.get("coord", {})
    
    return s_main, s_wind, coord

def show_current_weather_data(city,main,wind,coord):
    st.subheader(f"Current Weather in {city.capitalize()}")
    df = pd.DataFrame(
        [
            {"Temperature (°C)": f"{main["temp"]:.2f} °C",
            "Humidity": f"{main["humidity"]:.2f} %",
            "Wind speed (m/s)": f"{wind["speed"]:.2f} m/s"}
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