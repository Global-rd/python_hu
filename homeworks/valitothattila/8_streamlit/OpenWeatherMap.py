import streamlit as st
import pandas as pd
import requests
import plotly.express as px

API_KEY = st.secrets["OpenWeatherMap"]["api_key"]
BASE_URL = "https://api.openweathermap.org/data/2.5/"

#------------ Aktuális adatok lekérése ------------
@st.cache_data(ttl=86400)
def actual_weather_data_request(city):
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        st.warning(f"Something wrong! Error code: {response.status_code}")
        return None


#------------ Fejlécek és beviteli mező ------------
st.title("Robot Dreams Python - Weather Map & Data Visualization App")
city = st.text_input("City name:", placeholder="Enter city name:")

#----------- API működtetése
if city:
    data = actual_weather_data_request(city)
    if data:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        coords = data["coord"]                                      #------------ Koordináták lekérése a térkép miatt
        st.title(f"Current Weather in {city.capitalize()}:")
        kpi1, kpi2, kpi3 = st.columns(3)                            #------------ Adatok oszlopba rendezése
        with kpi1:    
            st.metric(label="Temperature (°C)", value=f"{temp}°C")
        with kpi2:
            st.metric(label="Humidity (%)", value=f"{humidity}%")
        with kpi3:
            st.metric(label="Wind speed (m/s)", value=f"{wind_speed} m/s")
        st.subheader("Weather Map")
        weather_map_vis_data = pd.DataFrame([{"lat": coords["lat"], "lon": coords["lon"]}])
        st.map(weather_map_vis_data)
    else:
        st.warning("No data has been received!")
else:
    st.info("Waiting for the name of the city!")