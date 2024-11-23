import pandas as pd

#CREATING DATAFRAMES 
#from 2 ore more series with the same index

s1 = pd.Series([1,2,3], index=["a","b","c"])
s2 = pd.Series([4,5,6], index=["a","b","c"])

df = pd.DataFrame({'col1': s1, 'col2': s2})
print(df)

#from 2 ore more series with different indexes

s1 = pd.Series([1,2,3], index=["a","b","c"])
s2 = pd.Series([4,5,6], index=["b","c","d"])

df = pd.DataFrame({'col1': s1, 'col2': s2})
print(df)

df = df.fillna(0)
print(df)


#create dataframe from a dictionary:
data = {'ID': [1,2,3], 'Name': ['Alice', 'Bob', 'Dexter'], 'Age': [15,56,12]}
df = pd.DataFrame(data)
print(df)

#create dataframe from list of dictionaries:

data = [
    {'ID': 1, 'Name': 'Alice', 'Age': 15},
    {'ID': 1, 'Name': 'Alice', 'Age': 15},
    {'ID': 1, 'Name': 'Alice', 'Age': 15}
]

df = pd.DataFrame(data)
print(df)

#create dataframe list of list

data = [[1, 'Alice', 25], 
        [2, 'Bob', 56],
        [3, 'Dexter', 12]]
df = pd.DataFrame(data, columns=["ID", "Name", "Age"])
print(df)


#create dataframe from a csv:
supermarket_df = pd.read_csv("lessons/14/datasets/supermarket_sales.csv")
print(supermarket_df)

#create dataframe from a json:
df = pd.read_json("lessons/14/datasets/test.json")
print(df)

#converting

#with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#    print(supermarket_df)

data_as_list_of_dicts = df.to_dict(orient="records")
print(data_as_list_of_dicts)
data_as_dict_of_lists = df.to_dict(orient="list")
print(data_as_dict_of_lists)
data_as_list_of_lists = df.values.tolist()
print(data_as_list_of_lists)