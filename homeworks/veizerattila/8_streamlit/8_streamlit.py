""" Hozd létre a következő streamlit appot:
- A mintán látható KPI-ok/key metric-ek és a chart-ok mindenképp legyenek jelen az app-odban, az elrendezés és a design (színkombinációk, tabok, oszlopok stb) a te döntésed. 

A következőkre lesz szükséged:
- OpenWeatherMap API key: https://home.openweathermap.org/users/sign_in regisztrálj, és hozz létre egy saját API key-t (https://home.openweathermap.org/api_keys) amit a .streamlit mappában a secrets.toml-ben tárolsz, ahogy az órán tanultuk.
- Egy cache-elt function-re a jelenlegi időjárás lekéréséhez. Dokumentáció: https://openweathermap.org/current
- Tipp: mind a két endpoint-hoz használhatsz egy “q” paramétert, nem kell a lat és lon paramétereket megadnod.
    Példák:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    Így az url-be bekerülhet a felhasználó által megadott város. Az alábbi screenshotok alapján reprodukáld a teljes streamlit appot:

(...)

Működési elv:
- OK A felhasználónak képesnek kell lennie megadni egy létező város nevét.
- Az, hogy hol kéred be az inputot, rád van bízva (pl egy sidebaron, vagy ahogy a screenshoton látod).
- Ha az API hívás hibát dob, tudasd egy warning használatával a hibát.
- Minden városnévvel kapcsolatos text az oldalon dinamikusan változzon.
- A https://openweathermap.org/current endpoint-ról húzd le az órán tanult módon a megadott település jelenlegi hőmérsékletét, páratartalmát és a szél sebességét.
- Jelenítsd meg KPI-okként/key metric-enként ezeket az adatokat. 
- A /current response tartalmazni fogja a lat és lon paramétereket, ezeket felhasználva jeleníts meg egy térképet az st.map() segítségével (ennek önállóan utána kell járnod).

Deploy:
- Deployold az app-ot a Community Cloud–ra, és a PR-odnak legyen része a link.
- A deployment-hez létre kell hoznod egy saját public repository-t, mivel csak admin joggal rendelkező felhasználó deployolhat. Ettől függetlenül a robot_dreams repo-ba PR-ként be kell adni a házi kódját a megszokott módon.
"""

import pandas as pd
import requests
import streamlit as st
from datetime import datetime
import os

##############################################################################################
############## 1/ API URL ÉS FÜGGVÉNYEK FELÉPÍTÉSE ###########################################
##############################################################################################

API_KEY = st.secrets["openweathermap"]["api_key"]
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

############## 1/1: API kapcsolat felépítése ###############################################
@st.cache_data(ttl=120) # 2 perces cache
def fetch_current_weather(city):
    print(f"Fetch current weather for {city}")

    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error in fetching the data. Status code: {response.status_code}")
        st.error(f"Error message: {response.text}")
        return None

############## 1/2: API időjárási részadatok leszedése ######################################
def process_data(data):
    if data:
        main = data['main']
        wind = data['wind']
        coord = data['coord']
        result = { "temp": main['temp'],
                "hum": main['humidity'],
                "wind": wind['speed'],
                "lat": coord['lat'],
                "lon": coord['lon']
            }
        df = pd.DataFrame([result])
        return df

    else:
        st.error("No data available")
        return None


##############################################################################################
############## 2/ PROGRAMTÖRZS (DF, DATA VIZ, KPI, MAP ) #####################################
##############################################################################################

st.title("Robot Dreams Python - Weather Map & Visualization App") # Oldal címe

st.subheader("-- by A. Veizer -- ") # Oldal címe

city_input = st.text_input("Enter city name", "Budapest") # Város input bekérése. Alapértelmezett: Budapest

data = fetch_current_weather(city_input)

if data:
    df = process_data(data)
    st.subheader(f"Current Weather in {city_input.capitalize()}") # 'City' érték átdása subheader-nek

    if data is not None:
        ############## 2/1: időjárási KPI adatok megjelenítése: ##############################
        kpi1, kpi2, kpi3 = st.columns(3)
        with kpi1:
            st.metric(label="Tempreture (˙C)", value = df["temp"])
        with kpi2:
            st.metric(label="Humidity (%)", value = df["hum"])
        with kpi3:
            st.metric(label="Wind Speed (m/s)", value = df["wind"])

        ############## 2/2: térképes nézet megjelenítése: #####################################
        map_data = pd.DataFrame({"lat": [df["lat"].iloc[0]], "lon": [df["lon"].iloc[0]]})
        st.map(map_data)
else:
    st.error(f"No data available. Check the above error messages and try again.")


##############################################################################################
############## Kiegészítés: képernyő törlése: ################################################
##############################################################################################
current_datetime = datetime.now()
os.system("cls")
print(f"====== Előző futási eredmény törölve a képernyőről ekkor: {current_datetime}) ======")
print("------------------------------------------------------------------")
streamlit_run = "streamlit run 8_HomeWork_streamlit_data_viz/8_streamlit.py"
print(f"Copy-Paste and run the following string from Terminal:\n{streamlit_run}")