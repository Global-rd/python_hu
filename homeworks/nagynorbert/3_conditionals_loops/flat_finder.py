#homework - Nagy Norbert

fav_cities=["new york","san francisco"]

# define city
while True:
    city = input("Please enter in which city would you like to live:").strip().lower()
    if not city:
        print("User error, city has to be a valid city")
    else:
        print("Thanks, valid city input.")
        break

# define price
while True:
    price = float(input("Please define the amount of price of rented flat ($):"))
    if price <= 0:
        print("User error, the amount of price should be bigger than 0!")
    else:
        print("Thanks, valid price input.")
        break


def printout_message(city,price,move):
    if move:
        print(f"You can move to {city} with amount of {price} $")
    else:
        print(f"You can't move to {city} with amount of {price} $")

if city == "chicago":
    move = True
elif city == "washington":
    move = False
elif city in fav_cities:
    if price <= 4000:
        move = True
    else:
        move = False
elif price <= 3000:
    move = True
else:
    move = False

printout_message(city,price,move)