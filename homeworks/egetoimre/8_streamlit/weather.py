import streamlit as st
import requests
import pandas as pd

api_key = st.secrets["openweathermap"]["api_key"]

@st.cache_data(ttl=3600)
def get_current_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@st.cache_data(ttl=3600)
def get_weather_forecast(city):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

st.set_page_config(page_title="Időjárás", layout="wide")
st.title("Pillanatnyi időjárás")

city = st.sidebar.text_input("Keresett város:", "Szeged")

if city:
    weather_data = get_current_weather(city)

    if weather_data:
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        lat, lon = weather_data['coord']['lat'], weather_data['coord']['lon']

        col1, col2, col3 = st.columns(3)
        col1.metric("Hőmérséklet (°C)", f"{temp:.1f}")
        col2.metric("Páratartalom (%)", f"{humidity}%")
        col3.metric("Szélsebesség (m/s)", f"{wind_speed:.1f}")

        st.map(pd.DataFrame({"lat": [lat], "lon": [lon]}))

        forecast = get_weather_forecast(city)
        if forecast:
            st.subheader("5 napos előrejelzés")
            forecast_data = [
                {
                    "Dátum": item["dt_txt"],
                    "Hőmérséklet (°C)": item["main"]["temp"],
                    "Páratartalom (%)": item["main"]["humidity"],
                    "Szélsebesség (m/s)": item["wind"]["speed"],
                }
                for item in forecast["list"]
            ]
            forecast_df = pd.DataFrame(forecast_data)
            st.dataframe(forecast_df)
    else:
        st.warning("A város nem található. Kérem adjon meg másik várost!")