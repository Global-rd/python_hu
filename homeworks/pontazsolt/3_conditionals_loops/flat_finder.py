city = input ("Choose a city: ").lower()
rent = int(input ("Monthly price in USD: "))

if city == "new york" or city == "san fransisco":
    if rent < 4000:
        print(f"Sarah can move to a flat in {city}.")
    else:
        print(f" Sarah would not move to {city}, rent is too high.")

elif city == "washington":
    print(f"There is no way to Sarah moving to {city}.")

elif city == "chicago":
    print(f"The money doesn't matter, Sarah moving to {city} in any case.")
 
elif rent <= 3000:
    print(f"Sarah would move to {city} because the rent is affordable")
else:
    print(f"Sarah would not move to {city} because the rent is too high.")