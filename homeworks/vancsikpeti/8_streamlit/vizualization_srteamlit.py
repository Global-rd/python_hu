import streamlit as st
import weather_data_api as weather
import pandas as pd
import plotly.express as px

st.title("Robot Dreams Python - Weather Map & Data Vizualization App")

entered_city = st.text_input("Enter city name", "Pécs")

weather_data = weather.get_data(city=entered_city, method="weather")
forecast_data = weather.get_data(city=entered_city,method="forecast")

# kpy-s: temperature, humidity, wind speed
if weather_data:
    st.header(f"Current weather in {entered_city}")
    kpi1, kpi2, kpi3 = st.columns(3)
    #KPI
    with kpi1:
        st.metric(
            label = "Temperature (°C)", 
            value = f"{weather.get_teperature(weather=weather_data):.2f}°C")
    with kpi2:
        st.metric(
            label = "Humidity (%)", 
            value = f"{weather.get_humidity(weather=weather_data)}%")
    with kpi3:
        st.metric(
            label = "Wind Speed (m/s)", 
            value = f"{weather.get_wind_speed(weather=weather_data):.2f} m/s")

st.subheader("Weather Map")
st.map(weather.get_coordinates(weather=weather_data))

st.subheader("Temperature Trends (Next 5 Days)")

forcast_temp_dt = []
for day in forecast_data['list']:
    forcast_temp_dt.append({
        "datetime": day["dt_txt"],
        "temperature": day["main"]["temp"]
    })
forcast_temp_df = pd.DataFrame(forcast_temp_dt)
forcast_temp_df.set_index("datetime", inplace=True)

forecast_weather = px.line(forcast_temp_df, x=forcast_temp_df.index, y="temperature")
st.plotly_chart(forecast_weather)

#streamlit url: https://howistheweatherpeter.streamlit.app/