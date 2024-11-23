#Homework - Nagy Norbert
import coinGecko_public_API as coins
import pandas as pd

df = pd.DataFrame(coins.get_coins_data(data_per_page=250))
print(df)

print("1. Number of empty cells:")
print(df.isna().sum())

print("\n2. Whole market_cap sum:")
df_market_cap = df["market_cap"].sum()
print(f"Total price of market cap: {df_market_cap} {coins.params.get("vs_currency","Undefined")}")

print("\n3. First 50 crypto with current price:")
top_50_df = df.nlargest(50,"current_price")
print(top_50_df)

print("\n4. Desc. order by price_change_percentage_24h:")
top_50_df = top_50_df.sort_values("price_change_percentage_24h",ascending=False)
print(top_50_df)

print("\n5. New column - new_direction:")

def evaluate_new_direction_column(row):
    evaluated_data = row["price_change_percentage_24h"]
    if evaluated_data == 0:
        return "0"
    elif evaluated_data > 0:
        return "+"
    return "-"

top_50_df["change_direction"] = top_50_df.apply(evaluate_new_direction_column,axis=1)
print(top_50_df)


