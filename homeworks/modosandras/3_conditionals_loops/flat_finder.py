price = int(input("Albérlet ára: "))
city = input("Város: ")
koltozik = False

if city == "Chicago":
    koltozik = True

if price < 4000 and (city == "New York" or city == "San Francisco"):
    koltozik = True
elif price <=3000 and city != "Washington":
    koltozik = True

if koltozik:
    print(f"{city} városba költözik {price} lakbérért.")
else:
    print(f"Nem költözik {city} városba {price} lakbérért.")
