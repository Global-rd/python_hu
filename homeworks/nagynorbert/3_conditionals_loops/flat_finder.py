#homework - Nagy Norbert

fav_cities=["new york","san francisco"]

# define city
while True:
    city = input("Please enter in which city would you like to live:")
    if len(city) == 0 or city.isspace():
        print("User error, city has to be a valid city")
    else:
        print("Thanks, valid city inputs.")
        break

input_city = city.strip().lower()

# define price
while True:
    price = input("Please define the amount of price of rented flat ($):")
    input_price = float(price)
    if input_price <= 0:
        print("User error, the amount of price should be bigger than 0!")
    else:
        print("Thanks, valid price input.")
        break


def printout_message(city,price,move):
    if move:
        print(f"You can move to {city} with amount of {price} $")
    else:
        print(f"You can't move to {city} with amount of {price} $")

if input_city == "chicago":
    move = True
    printout_message(city,price,move)
elif input_city == "washington":
    move = False
    printout_message(city,price,move)
elif input_city in fav_cities:
    if input_price <= 4000:
        move = True
        printout_message(city,price,move)
    else:
        move = False
        printout_message(city,price,move)
elif input_price <= 3000:
    move = True
    printout_message(city,price,move)
else:
    move = False
    printout_message(city,price,move)