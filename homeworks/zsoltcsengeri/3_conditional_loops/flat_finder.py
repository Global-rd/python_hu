"""
This script asks the user (property agent) which city they can offer for Sarah to rent an apartment in.
Sarah has specific preferences based on the city:
- If the city is Washington, she hates it and will refuse to rent no matter the price.
- If the city is Chicago, she loves it so much that the price doesn't matter—she'll take it.
- If the city is New York or San Francisco, Sarah will rent if the price is less than $4000.
- For any other city, Sarah will only rent if the price is $3000 or less.
The program then provides feedback on whether Sarah would rent based on the city and rent price.
"""


# Character
SARAH = "Sarah"

# Tuple for New York and San Francisco
cities_to_consider = ("New York", "San Francisco")

# Get the city
rental_city = input(
    f"{SARAH}: Which city can you offer for renting an apartment in? ").strip().title()

# Immediate response for Washington and Chicago
if rental_city == "Washington":

    print(f"{SARAH}: Sorry, but I really don't like {rental_city}. No way!")
    rental_city = input(
        f"{SARAH}: Which city can you offer for renting an apartment in? ").strip().title()

if rental_city == "Chicago":

    print(f"{SARAH}: My favorite place is {
          rental_city}, so no matter how much the price is, I'll take it!")

# For other cities
else:
    apartment_rent_price = int(
        input(f"{SARAH}: Ok, and how much is the rent for the apartment in dollars? "))

    if rental_city in cities_to_consider:
        if apartment_rent_price < 4000:
            print(f"{SARAH}: Awesome! I like {
                  rental_city}, and the price is great. I'll take it!")
        else:
            print(f"{SARAH}: {rental_city} is amazing, but that's pretty expensive!")
    else:
        if apartment_rent_price <= 3000:
            print(f"{SARAH}: The rent in {
                  rental_city} is reasonable, so I'm interested!")
        else:
            print(f"{SARAH}: The rent in {
                  rental_city} is too high for me, so I'll pass.")
