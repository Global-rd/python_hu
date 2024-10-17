city = input ("Choose a city: ")
rent = int(input ("Monthly price in USD: "))

if city.lower() == "new york" or city.lower() == "san fransisco":
    if rent < 4000:
        print(f"Sarah can move to a flan in {city}.")
    else:
        print(f" Sarah would not move to {city}, rent is too high.")

elif city.lower() == "washington":
    print(f"There is no way to Sarah moving to {city}.")

elif city.lower() == "chicago":
    print(f"The money doesn't matter, Sarah moving to {city} in any case.")

else: 
    if rent <= 3000:
        print(f"Sarah would move to {city} because the rent is affordable")
    else:
        print(f"Sarah would not move to {city} because the rent is too high.")