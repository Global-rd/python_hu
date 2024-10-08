"""
This script asks the user (property agent) which city they can offer to rent an apartment in.
If the city is Washington or Chicago, it gives an immediate response 
because Sarah hates Washington and loves Chicago, so price doesn't matter.
For other cities, Sarah asks for the rent price and provides feedback accordingly.
"""

# Characters
sarah = "Sarah"
agent = "Property Agent"

# Get the city
rental_city = input(
    f"{sarah}: Which city can you offer for renting an apartment in? ")

# Immediate response for Washington and Chicago
if rental_city == "Washington":
    print(f"{agent}: The city is {rental_city}.")
    print(f"{sarah}: Sorry, but I really don't like {rental_city}. No way!")
    rental_city = input(
        f"{sarah}: Which other city can you offer for renting an apartment in? ")

if rental_city == "Chicago":
    print(f"{agent}: The city is {rental_city}.")
    print(f"{sarah}: My favorite place is {
          rental_city}, so no matter how much the price is, I'll take it!")

# For other cities
else:
    apartment_rent_price = int(
        input(f"{sarah}: Ok, and how much is the rent for the apartment in dollars? "))

    print(f"{agent}: So, this apartment in {
          rental_city} is {apartment_rent_price} dollars.")

    if rental_city == "New York" or rental_city == "San Francisco":
        if apartment_rent_price < 4000:
            print(f"{sarah}: Awesome! I love {
                  rental_city}, and the price is great. I'll take it!")
        else:
            print(f"{sarah}: {rental_city} is amazing, but that's pretty expensive!")
    else:
        if apartment_rent_price <= 3000:
            print(f"{sarah}: The rent in {
                  rental_city} is reasonable, so I'm interested!")
        else:
            print(f"{sarah}: The rent in {
                  rental_city} is too high for me, so I'll pass.")
