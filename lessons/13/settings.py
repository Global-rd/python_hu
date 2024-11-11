import os
import dotenv
from dotenv import load_dotenv
load_dotenv()

#API_KEY
OPENWEATHERMAP_API_KEY = os.environ.get("OPENWEATHERMAP_API_KEY")

#COORDINATES
BUDAPEST = {"lat":47.4979, "lon": 19.0402}