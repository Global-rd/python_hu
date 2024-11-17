"""
This script fetches the top 250 cryptocurrencies by market cap from the CoinGecko API,
converts the JSON response into a Pandas DataFrame, and saves it as a CSV file.

Steps:
1. Sends a GET request to the CoinGecko API.
2. Parses the JSON response and converts it to a Pandas DataFrame.
3. Saves the DataFrame to a CSV file for further analysis.

"""

import requests
import pandas as pd

# URL for the CoinGecko API endpoint
url = "https://api.coingecko.com/api/v3/coins/markets"

# Parameters to fetch the top 250 cryptocurrencies by market cap in USD
params = {"vs_currency": "usd", "per_page": "250"}

# Headers for the API request (optional for this endpoint)
headers = {"accept": "application/json"}

# API call to fetch cryptocurrency data
response = requests.get(url=url, params=params, headers=headers)

# Parse the response JSON and pretty-print it
data = response.json()  # Convert the response to a Python dictionary
# print(json.dumps(data, indent=4))  # Pretty-print with indentation

# Convert the Python dictionary data to DataFrame
df = pd.DataFrame(data)
print(df)

# Save a DataFrame to a CSV file
# The CSV file will contain the full list of 250 cryptocurrencies
df.to_csv(
    "crypto_list_250.csv", index=False
)  # index=False prevents an index column from being added
