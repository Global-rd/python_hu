"""
This code uses Streamlit to create an interactive web app that:

Allows the user to input a city name.
Fetches weather data for that city using fetch_weather.
Displays weather information (e.g., temperature, humidity).
Shows a map centered on the city using pydeck.
"""


import streamlit as st
from temp_humidity_wind_api_call import fetch_weather #Imports the fetch_weather function from the first file
import pydeck as pdk #Pydeck is a library for creating interactive maps in Streamlit

# Set up the title of the app
st.title("Robot Dreams Python - Weather Map & Data Visualization APP")

# Input for city name where "London" is the default value
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

        # Get latitude and longitude for the city
        latitude = data["coord"]["lat"]
        longitude = data["coord"]["lon"]

        # Weather map display using pydeck
        st.subheader("Weather Map")
        layer = pdk.Layer(
            "ScatterplotLayer",
            data=[{"lat": latitude, "lon": longitude}],
            get_position=["lon", "lat"],
            get_color="[200, 30, 0, 160]",
            get_radius=1000,
        )
        view_state = pdk.ViewState(
            latitude=latitude,
            longitude=longitude,
            zoom=8,
            pitch=0,
        )

        # Render map
        st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

    else:
        # Display an error message if the API call fails
        st.error(data.get("message", "Error fetching data"))
