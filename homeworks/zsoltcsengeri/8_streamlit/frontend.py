import streamlit as st
from openweather_api_call import fetch_weather

# Set up the title of the app
st.title("Robot Dreams Python - Weather Map & Data Visualization APP")

# Input for city name
city = st.text_input("Enter the city name", "London")

# Fetch and display weather data
if city:
    data = fetch_weather(city)
    
    # Check if the API call was successful
    if data.get("cod") == 200:
        # Extract weather information
        temperature = f"{data['main']['temp']}°C"
        feels_like = f"{data['main']['feels_like']}°C"
        humidity = f"{data['main']['humidity']}%"
        wind_speed = f"{data['wind']['speed']} m/s"

        # Display in horizontal columns
        st.header(f"Weather in {data['name']}, {data['sys']['country']}")
        col1, col2, col3 = st.columns(3)

        col1.metric("Temperature", temperature, f"Feels like {feels_like}")
        col2.metric("Humidity", humidity)
        col3.metric("Wind Speed", wind_speed)
        
    else:
        # Display an error message if the API call fails
        st.error(data.get("message", "Error fetching data"))
