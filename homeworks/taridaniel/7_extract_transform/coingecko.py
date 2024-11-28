import requests
import pandas as pd

# Step 1: Fetch the data from the CoinGecko API
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 250,
    "page": 1
}
response = requests.get(url, params=params)
data = response.json()

# Step 2: Store the data in a pandas DataFrame
df = pd.DataFrame(data)

# Task 1: Determine how many empty cells can be found in each column of the DataFrame and print them
empty_cells = df.isnull().sum()
print("Empty cells in each column:")
print(empty_cells)

# Task 2: Determine the sum of market_cap to the whole DataFrame and print it
total_market_cap = df['market_cap'].sum()
print("\nTotal market cap:", total_market_cap)

# Task 3: Create a new DataFrame with the name top50_df containing only the first 50 cryptocurrencies according to current_price
top50_df = df.nlargest(50, 'current_price')

# Task 4: Order top50_df according to price_change_percentage_24h in descending order
top50_df = top50_df.sort_values(by='price_change_percentage_24h', ascending=False)

# Task 5: Create a new column in top50_df named change_direction with values based on price_change_percentage_24h
def determine_direction(change):
    if change > 0:
        return "+"
    elif change < 0:
        return "-"
    else:
        return "0"

top50_df['change_direction'] = top50_df['price_change_percentage_24h'].apply(determine_direction)

# Print the final DataFrame
print("\ntop50_df:")
print(top50_df)

