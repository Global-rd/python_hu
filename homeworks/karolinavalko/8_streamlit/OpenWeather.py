import streamlit as st
import pandas as pd
import requests



API_KEY = st.secrets["openweathermap"]["api_key"]
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast?"


    

@st.cache_data(ttl=900)
def fetch_forecast_city(city):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})
    if response.status_code == 200:
        return response.json()
    else:
        st.warning(f"This city is not in our database. Please try another city for weather forecast.")
        return None

def current_weather_data(data):
    try:
        return {
            "Temperature (°C)": round(data["main"]["temp"],2,),
            "Humidity (%)": round(data["main"]["humidity"],0,),
            "Wind Speed (m/s)": round(data["wind"]["speed"],2,),
            "Latitude": data["coord"]["lat"],
            "Longitude": data["coord"]["lon"],         
        }   
    except KeyError as e:
        print(f"Something unexpected happened: {e}")

@st.cache_data(ttl=300)
def fetch_weather_city(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})
    if response.status_code == 200:
        return current_weather_data(response.json())
    else:
        st.error(f"This city is not in our database. Please try another city for current weather.")
        return None    




st.title("Robot Dreams Python - Weather Map & Data Visualization App")
city = st.text_input("Enter city name")


st.button("Get weather")
if city:
    weather = fetch_weather_city(city)
    if weather:
        st.subheader(f"Current Weather in {city}")
        labels= list(weather.keys())
        values= list(weather.values())
        col1, col2, col3 =st.columns(3)
        col1.metric(labels[0], f"{values[0]}°C")
        col2.metric(labels[1], f"{values[1]}%")
        col3.metric(labels[2], f"{values[2]} m/s")

df =pd.DataFrame(weather, index= [0])
st.map(df, latitude="Latitude", longitude="Longitude", zoom=10,)
           

