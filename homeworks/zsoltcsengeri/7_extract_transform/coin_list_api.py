import requests
import json
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "per_page": "250"
}

headers = {"accept": "application/json"}

response = requests.get(url=url, params=params, headers=headers)

# Parse the response JSON and pretty-print it
data = response.json()  # Convert the response to a Python dictionary
#print(json.dumps(data, indent=4))  # Pretty-print with indentation

# Convert the Python dictionary data to DataFrame
df = pd.DataFrame(data)
print(df)

#save a DataFrame to a CSV file
df.to_csv('./coin_list_250.csv', index=False) #index=False prevents an index column from being added