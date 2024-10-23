import time # altough it was not in the homework description, I like using it :)

# request the city name and the rent fee
city = input("Please enter the name of the city where you want to rent a flat: ").strip().lower()
"""
it can be a problem if the user enters empty characters (spaces) between the letters of the specified cities example: "CHI  cago", as the program will handle as a different city
"""

# asking to input, and checking wether the rent fee is positive
while True:
    try:
        rent = int(input("Please enter the monthly rent fee of the flat in USD (don't use dots): ")) # immediately converts it integer to make it possible the compare with an integer
        if rent > 0:
            break
        else:
            print("The rent fee is less than zero, plesae enter a positive number!")
    except ValueError:
        print("Invalid number, please give a valid one." )

# decision making, printed capitalized
if city == "chicago":
    time.sleep(1)
    print(f"Sarah loves Chicago, so she will definitely move there, no matter how much the rent is.")
elif city in ["new yoek", "san fransisco"]:
    if rent < 4000: # integer already converted in row 6
        time.sleep(1)
        print(f"Sarah could move to {city.capitalize()} because the rent is less than 4.000 USD.")
    else:
        time.sleep(1)
        print(f"Sarah would not move to {city.capitalize()} because the rent is too high.")
elif city == "washington":
    time.sleep(1)
    print(f"Sarah hates Washington, so she wouldn't move there for any money.")
elif rent <= 3000: # integer already converted in row 6
    time.sleep(1)
    print(f"Sarah could move to {city.capitalize()} because the rent is right.")
else:
    time.sleep(1)
    print(f"Sarah would not move to {city.capitalize()} because the rent is too high.")