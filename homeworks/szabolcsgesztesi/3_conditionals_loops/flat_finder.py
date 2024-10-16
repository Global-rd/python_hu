
good_cities = ["New York", "San Fransisco"]
worst_city = "Washington"
best_city = "Chicago"

city = input("Kérem adja meg a várost: ")
price = int(input("Kérem adja meg a havi lakbér árát (USD): "))

if city == best_city:
    print(f"Sarah kedvenc városa {best_city}, bármi pénzert odaköltözne.")
elif city == worst_city:
    print(f"Sajnos Saharah számára {worst_city} elfogadhatatlan.")
elif city in good_cities:
    if price < 4000:
        print(f"{city} elfogadható Sarah számára {price} dollárért.")
    else:
        print(f"{city} nem elfogadható Sarah számára {price} dollárért.")
else:
    print(f"{city} {'elfogadható' if price < 3000 else 'nem elfogadható'} Sarah számára {price} dollárért.")