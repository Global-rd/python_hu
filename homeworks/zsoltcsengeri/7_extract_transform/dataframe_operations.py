"""
This script performs the following operations:
1. Reads cryptocurrency data from a CSV file into a DataFrame.
2. Counts empty cells in each column and prints the results.
3. Calculates the total market capitalization and prints the result.
4. Creates a new DataFrame ('top50_df') with the top 50 cryptocurrencies by current price.
5. Sorts 'top50_df' by 24-hour price change percentage in descending order.
6. Adds a new column 'change_direction' to indicate the direction of price change (+, -, 0).
7. Saves the final DataFrame to a CSV file for further use.

"""

from coin_list_api import data  # Import data from the API call script
import pandas as pd

# *1 Determine
# How many empty cells are in each column of the DataFrame
# and print the result

df = pd.read_csv("crypto_list_250.csv")


# Count the number of empty (NaN) cells in each column
empty_cells_per_column_df = df.isnull().sum()

# Print the result
print(f"Number of empty cells in each column:{empty_cells_per_column_df}")

# Optional: Save the empty cell counts to a CSV file
empty_cells = empty_cells_per_column_df.to_csv(
    "empty_cells.csv", header=["empty_cells"]
)

# *2 Determine
# the market_cap total sum in the DataFrame
# and print the result

# Calculate the total market capitalization
total_market_cap_df = df["market_cap"].sum()
print(f"the total market_cap value: {total_market_cap_df}")

# *3 Create
# A new DataFrame as 'top50_df'
# Store the first 50 cryptocurrencies based on their 'current_price'
top50_df = df.sort_values("current_price", ascending=False).head(50)
print(top50_df)

# *4 Sort
# The 'top50_df' based on 'price_change_percentage_24h' in descending order
top50_df = top50_df.sort_values("price_change_percentage_24h", ascending=False)
print(top50_df)

# *5 Create
# A new column in 'top50_df' called 'change_direction'
# This column indicates the direction of the 24-hour price change
# + for positive, - for negative, 0 for no change


# Define a helper function to determine the change direction
def change_direction_column(row):
    if row["price_change_percentage_24h"] > 0:
        return "+"
    elif row["price_change_percentage_24h"] < 0:
        return "-"
    else:
        return "0"


# Apply the helper function to each row to create the new column
top50_df["change_direction"] = top50_df.apply(change_direction_column, axis=1)
print(top50_df)


# Optional: Save the final DataFrame to a CSV file
top50_df.to_csv("change_direction.csv")
