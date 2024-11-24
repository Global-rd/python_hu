'''
Segítő file a weather_logs.db olvasásához
'''

import pandas as pd
from db_connector import SqliteDB

with SqliteDB('weather_logs.db') as db:
    df = db.select_records("SELECT * FROM searches")
    print(df)
