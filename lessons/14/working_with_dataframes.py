import pandas as pd

df = pd.read_csv("lessons/14/datasets/supermarket_sales.csv")
print(df.dtypes)
print(df.info())

print(df.head(20))
print(df.tail(15))

print(df.describe())

#selecting columns:
product_price_df = df[['Product line', 'Unit price']]
print(product_price_df)
print(type(product_price_df['Product line']))

#loc
print("-----------------")
print(df.loc[1, 'Product line'])
print(df.loc[1:3, ['Product line', 'Unit price']])

#.iloc
print("-----------------")
print(df.iloc[1, 1])
print(df.iloc[1:3, [1,2]])

#aggregation and grouping:

#total sales per city and product line:
total_sales_df = df.groupby(['City', 'Product line'])['Total'].sum().reset_index()
print(total_sales_df)

avg_rating_df = df.groupby(['Customer type', 'Payment'])['Rating'].mean().reset_index()
print(avg_rating_df)


#filtering
yangon_df = df[df['City'] == 'Yangon']
print(yangon_df)


#method chaining
result_df = (
    df[df['City'] == 'Yangon'] 
    .groupby('Gender')
    .agg({'Unit price': 'mean'})
    .reset_index()
    .sort_values('Unit price', ascending=False)
)

print(result_df)


#read stock dataframes
df_stock_base = pd.read_csv("lessons/14/datasets/stock_base.csv")
df_stock_extension = pd.read_csv("lessons/14/datasets/stock_extension.csv")
print(df_stock_base)
print(df_stock_extension)

merged_df = pd.merge(df_stock_base, df_stock_extension, on="id", how="left")
print(merged_df)

merged_df["total_value"] = merged_df["price"] * merged_df["quantity"]
print(merged_df)

def categorize_stock(row):
    if row["price"] > 1000:
        return 'Premium'
    else:
        return 'Standard'

merged_df["category"] = merged_df.apply(categorize_stock, axis=1)
print(merged_df)

#EFFECTIVE PANDAS - MATT HARRISON
