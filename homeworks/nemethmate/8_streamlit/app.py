import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import sqlite3
import toml

# Inicializáljuk az adatbázist
def init_db():
    conn = sqlite3.connect('weather_logs.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            city TEXT,
            temperature REAL,
            humidity REAL,
            wind_speed REAL,
            timestamp DATETIME
        )
    ''')
    conn.commit()
    conn.close()

# Adatok logolása az adatbázisba
def log_weather(city, temperature, humidity, wind_speed):
    conn = sqlite3.connect('weather_logs.db')
    c = conn.cursor()
    c.execute('INSERT INTO logs VALUES (?, ?, ?, ?, ?)', 
              (city, temperature, humidity, wind_speed, datetime.now()))
    conn.commit()
    conn.close()

# API kulcs betöltése a teljes elérési útvonal megadásával
secrets_path = r"C:\Users\veszperenyine\Documents\GitHub\python_hu\homeworks\nemethmate\8_streamlit\secrets.toml"
secrets = toml.load(secrets_path)
api_key = secrets['api']['key']

# Kezdő oldal
st.title("Időjárás Dashboard 🌤️")

# Város név bekérése
city = st.text_input("Add meg egy város nevét:")

if city:
    # Aktuális időjárás API hívás
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Adatok kinyerése az API válaszból
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        lat = data['coord']['lat']
        lon = data['coord']['lon']

        # KPI-ok megjelenítése
        st.subheader(f"Időjárás {city} városában:")
        col1, col2, col3 = st.columns(3)
        col1.metric("Hőmérséklet (°C)", f"{temp}°C")
        col2.metric("Páratartalom (%)", f"{humidity}%")
        col3.metric("Szélsebesség (m/s)", f"{wind_speed} m/s")

        # Térkép megjelenítése
        st.map(pd.DataFrame({'lat': [lat], 'lon': [lon]}))

        # Adatok logolása
        log_weather(city, temp, humidity, wind_speed)

        # Előrejelzés (extra)
        forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
        forecast_response = requests.get(forecast_url)
        if forecast_response.status_code == 200:
            forecast_data = forecast_response.json()
            st.subheader("3 órás időjárás előrejelzés:")
            for item in forecast_data['list'][:5]:  # Az első 5 előrejelzést mutatjuk
                time = item['dt_txt']
                temp = item['main']['temp']
                desc = item['weather'][0]['description']
                st.write(f"{time}: {temp}°C, {desc}")
        else:
            st.warning("Nem sikerült lekérni az előrejelzési adatokat.")
    else:
        st.warning("Nem sikerült lekérni az időjárási adatokat. Ellenőrizd a város nevét.")
else:
    st.info("Adj meg egy városnevet az időjárási adatok megtekintéséhez.")

# Az adatbázis inicializálása
init_db()
