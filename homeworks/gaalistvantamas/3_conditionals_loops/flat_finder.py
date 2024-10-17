"""
Author: Gaál István Tamás
Task: Homework-3 / 1 
"""

NEW_YORK_AND_SAN_FRANCISCO_LIMIT = 4000
OTHER_CITIES_LIMIT = 3000

place_and_price = input(
    "Please give a city and the monthly fee, separated by a coma!\n").split(",")

place = place_and_price[0].title()
price = int(place_and_price[1])
print(f" {place} : {price}")

if (place == "New York" or place == "San Francisco") and (price < NEW_YORK_AND_SAN_FRANCISCO_LIMIT):
    print(f"The conditions are OK for her! The name of the city: {
          place} and the monthly fee is {price}.")
elif place == "Washington":
    print(f"She doesn't want to live in {place}!")
elif place == "Chicago":
    print(f"She wants to live here, the money doesn't matter!")
elif price < OTHER_CITIES_LIMIT:
    print(f"This place: {place}, for that monthly fee {price} is OK for her.")
else:
    print("These conditions are not appropriate for her!")
