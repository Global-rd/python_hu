from coin_list_api import data
import pandas as pd

# *1 Determine
# how many empty cells are in each column of the DataFrame
# and print the result

df = pd.read_csv("crypto_list_250.csv")


# Count the number of empty (NaN) cells in each column
empty_cells_per_column_df = df.isnull().sum()

# Print the result
print(f"Number of empty cells in each column:{empty_cells_per_column_df}")

empty_cells = empty_cells_per_column_df.to_csv(
    "empty_cells.csv", header=["empty_cells"]
)

# *2 Determine
# the market_cap total sum in the DataFrame
# and print the result
total_market_cap_df = df["market_cap"].sum()
print(f"the total market_cap value: {total_market_cap_df}")

# *Create
# a new DataFrame as top50_df
# store the first 50 crypto currencies based on the current_price
top50_df = df.sort_values("current_price", ascending=False).head(50)
print(top50_df)

# *Sort
# top50_df based on price_change_percentage_24h in descending order
top50_df = top50_df.sort_values("price_change_percentage_24h", ascending=False)
print(top50_df)

# * Create
# a new coloumn the top50_df with the name of change_direction whose can have 3 values:
# Ha a price_change_percentage_24h értéke nagyobb mint 0, az oszlop értéke legyen “+”
# Ha negatív, az oszlop értéke legyen “-“
# Ha kereken 0, az érték legyen “0”


def change_direction_column(row):
    if row["price_change_percentage_24h"] > 0:
        return "+"
    elif row["price_change_percentage_24h"] < 0:
        return "-"
    else:
        return "0"


top50_df["change_direction"] = top50_df.apply(change_direction_column, axis=1)
print(top50_df)

top50_df.to_csv("change_direction.csv")
