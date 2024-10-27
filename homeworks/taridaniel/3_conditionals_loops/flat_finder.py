city = input("Please enter an American city: ").title()
price = int(input("Please enter the price (USD): "))

if city in ["New York", "San Francisco"] and price < 4000:
    print(f"I like these conditions in {city}, I want to live here")
elif city == "Washington": 
    print(f"I hate {city}, I don't want to live in this city")
elif city == "Chicago":
    print(f"I love {city} so much! The price of the rent doesn't matter, I want to live here!")
elif price <= 3000:
    print(f"It's okay, this will work in {city} for me with these conditions")
else:
    print("I don't like these conditions")