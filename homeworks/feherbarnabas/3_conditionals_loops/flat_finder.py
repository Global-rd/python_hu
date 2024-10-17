city = input("Type a name of a city to live in: ")
rent = int(input("How much is the rent in USD for a month? "))

if ( city in ["New York", "San Fransisco"] and rent < 4000 ):
    print(f"You can live in {city} for {rent} USD.")

elif city == "Washington":
    print(f"You know it's {city} so you better keep that {rent} USD.")

elif city == "Chicago":
    print(f"It's {city} you will have to pay much more than {rent} USD for a month because you really would like to live there.")

elif rent <= 3000:
    print(f"It's cheap so you can live in {city} for {rent} USD.")

else: 
    print(f"Look for another city because there are no flats in {city} for {rent} USD.")