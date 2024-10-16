# input data (city and rental fee)
city = input("In which city are you looking for a flat to rent? ").strip().title()
rental_fee = int(input("What is the rental fee (USD)? "))

# close out Washington
if city == "Washington":
    print(f"You cannot rent a flat in {city} for {rental_fee} USD")
# Chicago for any price
elif city == "Chicago":
    print(f"You can rent a flat in {city} for {rental_fee} USD")
# New York / San Francisco case
elif city in ["New York", "San Francisco"]:
    if rental_fee < 4000:
        print(f"You can rent a flat in {city} for {rental_fee} USD")
    else:
        print(f"You cannot rent a flat in {city} for {rental_fee} USD")
# all other cases            
elif rental_fee <= 3000:
    print(f"You can rent a flat in {city} for {rental_fee} USD")
else:
    print(f"You cannot rent a flat in {city} for {rental_fee} USD")