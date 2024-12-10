import streamlit as st
import requests
import pandas as pd

# Load API key from secrets
API_KEY = st.secrets["api_key"]

@st.cache_data(ttl=600)
def fetch_weather_data(city, endpoint):
    url = f'http://api.openweathermap.org/data/2.5/{endpoint}?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.warning(f"Error fetching data from {endpoint}.")
        st.write(f"Status Code: {response.status_code}")
        st.write(f"Response: {response.text}")
        return None

def get_current_weather(city):
    return fetch_weather_data(city, 'weather')

def get_weather_forecast(city):
    return fetch_weather_data(city, 'forecast')

def display_weather_data(city):
    current_weather = get_current_weather(city)
    if current_weather:
        st.subheader(f"Current Weather in {city}")
        st.metric(label="Temperature", value=f"{current_weather['main']['temp']} °C")
        st.metric(label="Humidity", value=f"{current_weather['main']['humidity']} %")
        st.metric(label="Wind Speed", value=f"{current_weather['wind']['speed']} m/s")
        
        # Show map
        lat, lon = current_weather['coord']['lat'], current_weather['coord']['lon']
        st.map(pd.DataFrame([[lat, lon]], columns=['lat', 'lon']))

def display_forecast_data(city):
    forecast = get_weather_forecast(city)
    if forecast:
        st.subheader(f"Temperature Trends (Next 5 Days) for {city}")

        df = pd.DataFrame(forecast['list'])
        df['datetime'] = pd.to_datetime(df['dt'], unit='s')
        df.set_index('datetime', inplace=True)

        df['temp'] = df['main'].apply(lambda x: x['temp'])

        if 'temp' in df.columns:
            st.line_chart(df[['temp']])
        else:
            st.warning("Temperature data is missing from the forecast data.")

# Main App
st.title("Weather Dashboard")

city = st.text_input("Enter a city name:")

if city:
    display_weather_data(city)
    display_forecast_data(city)

