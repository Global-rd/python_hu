city = input("What's the city? ")
rent_price = int(input("How much does the apartment cost? "))

print(city, rent_price)

if city == "Washington":
    print(f" Sorry but I hate {city} so, no way!")

elif city == "New York" or city == "San Francisco":
    if rent_price < 4000:
        print(f"Cool!!! I love {city} so, I want it now!!!")
    elif rent_price >= 4000:
        print("Nice but expensive!")

else:
    if rent_price < 3000:
        print(f"For {city} this price is reasonable, so I want it!")
    elif rent_price > 3000:
        print(f" For {city} this price is too high, so no thanks!")
