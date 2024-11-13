import pandas as pd


#read from list:
s_from_list = pd.Series(["1",2,3,4])
print(s_from_list)
s_from_list = s_from_list.astype("string")
print(s_from_list)

#read from dictionary:
s = pd.Series({'a': 1, 'b': 2, 'c':3})
print(s)


#indexing
s = pd.Series([10,30,20], index=['a', 'b', 'c'])
print(s)

#limiting with indexes
calories = {'day1': 2000, 'day2': 1800, 'day3': 5000}

s = pd.Series(calories, index=["day1", "day2"])
print(s)

#vectorization
s = pd.Series([1,2,3,4])
print(s + 2)

#conditional vectorization
s = s + 2 * (s % 3 == 0)
print(s)


#truthy-falsy value
#0 -> False
#1 -> True

"""
1 + 2 * 0
2 + 2 * 0
3 + 2 * 1
4 + 2 * 0
"""