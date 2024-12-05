import sqlite3
from datetime import datetime

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

def log_weather(city, temperature, humidity, wind_speed):
    conn = sqlite3.connect('weather_logs.db')
    c = conn.cursor()
    c.execute('INSERT INTO logs VALUES (?, ?, ?, ?, ?)', 
              (city, temperature, humidity, wind_speed, datetime.now()))
    conn.commit()
    conn.close()
