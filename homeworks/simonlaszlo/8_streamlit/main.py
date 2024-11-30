import streamlit as st
import requests
import datetime
import folium
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
import time

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = st.secrets["polygon"]["api_key"]

 # késleltetés, csak delay_sec -enként lehessen lekérni Ha frissíti az oldalt, akkor is várnia kell.
DELAY_SEC = 10  # másodpercben

if "delay_starttime" not in st.session_state:
    st.session_state.delay_starttime = time.time()

# Ellenőrizzük, hogy eltelt-e az idő
delay_elapsed = time.time()- st.session_state.delay_starttime
delay_remaining= DELAY_SEC - delay_elapsed

@st.cache_data(ttl=600)
def get_weather(city): # az aktuális adatok
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric', 
        'lang': 'hu'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        st.error(f"Error fetching data: {data['message']}")
        return None

    return {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'weather': data['weather'][0]['description'],
        'date': datetime.datetime.now(),
        'wind_speed': data['wind']['speed'], 
        'coord': {
            'lat': data['coord']['lat'],
            'lon': data['coord']['lon']
        }
    }

@st.cache_data(ttl=600)
def get_forecast(city): # előrejelzés
    params = {
        'q': city,
        'appid': API_KEY,
        'units':'metric',
        'lang': 'hu'
    }
    response = requests.get(FORECAST_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        st.error(f"Error fetching forecast data: {data['message']}")
        return None

    forecast_data = []  
    for item in data['list']:
        forecast_data.append({
            'date': datetime.datetime.fromtimestamp(item['dt']),
            'temperature': item['main']['temp'],
            'wind_speed': item['wind']['speed'],
            'weather': item['weather'][0]['description']
        })

    return forecast_data

def create_map(lat, lon): # koordináták alapján létrehozza a térképet.
    city_map = folium.Map(location=[lat, lon], zoom_start=12)    
    folium.Marker(
        location=[lat, lon],
        popup='Város',
        icon=folium.Icon(color='blue')
    ).add_to(city_map)
    return city_map

st.title("Helyi időjárás")
city = st.text_input("Add meg a város nevét:", "Szőreg")

if st.button("Időjárás lekdezése"):
    if delay_remaining <= 0:
        st.session_state.delay_starttime = time.time()  # frissítjük a kezdési időt
        weather_data = get_weather(city)
        if weather_data:
            lat_ = weather_data['coord']['lat'] # a város koordinátái kellenek a térképhez
            lon_ = weather_data['coord']['lon']
            wind_speed_kmh = int(weather_data['wind_speed'] * 3.6)
            st.subheader(f"Időjárás {weather_data['city']} helységben")
            st.header(f"Időjárás leírás: {weather_data['weather']}")
            col1, col2, col3 = st.columns(3)
            col1.metric("Hőmérséklet", f"{weather_data['temperature']}°C")
            col2.metric("Páratartalom", f"{weather_data['humidity']}%")
            col3.metric("Szélsebesség", f"{wind_speed_kmh} km/h")
            
            st.write(f"Dátum: {weather_data['date'].strftime('%Y-%m-%d %H:%M:%S')}")            
            city_map = create_map(lat_, lon_)
            folium_static(city_map)

            forecast_data = get_forecast(city)   
            if forecast_data:  # Grafikon létrehozása
               
                dates = [entry['date'] for entry in forecast_data]
                temperatures = [entry['temperature'] for entry in forecast_data]
                wind_speeds = [(entry['wind_speed'] * 3.6) for entry in forecast_data]  # m/s -> km/h

                fig, ax1 = plt.subplots()
                color = 'tab:red'
                ax1.set_xlabel('Dátum')
                ax1.set_ylabel('Hőmérséklet (°C)', color=color)
                ax1.plot(dates, temperatures, color=color, label='Hőmérséklet (°C)')
                ax1.tick_params(axis='y', labelcolor=color)

                ax2 = ax1.twinx()
                color = 'tab:blue'
                ax2.set_ylabel('Szélsebesség (km/h)', color=color)
                ax2.plot(dates, wind_speeds, color=color, label='Szélsebesség (km/h)')
                ax2.tick_params(axis='y', labelcolor=color)                
                fig.suptitle('5 napos időjárás előrejelzés')  
                fig.tight_layout()
                st.pyplot(fig)

    else:
        st.warning(f"Még {int(delay_remaining)} másodpercet kell várni a következő lekérdezésig.")