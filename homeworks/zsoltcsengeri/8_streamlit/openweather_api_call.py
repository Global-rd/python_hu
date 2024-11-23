import requests
import streamlit as st
import json


def fetch_weather(city: str):
    """
    Fetch weather data for a given city using the OpenWeather API.

    Args:
        city (str): The name of the city to fetch the weather for.

    Returns:
        dict: The JSON response from the OpenWeather API.
    """
    # Get API key from Streamlit secrets
    API_KEY = st.secrets["openweather"]["api_key"]
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    # Parameters to fetch data by city name
    params = {
        "q": city,
        "units": "metric",
        "appid": API_KEY,
    }

    # Make the API call
    response = requests.get(url=BASE_URL, params=params)

    # Return the parsed JSON response
    return response.json()


# Call the function fetch_weather() passing city name like London
data = fetch_weather("London")
print(json.dumps(data, indent=4))  # Pretty-print with indentation
