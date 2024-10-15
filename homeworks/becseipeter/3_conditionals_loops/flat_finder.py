city = input("Choose your city\n")
rent = int(input("How much is the rent?\n"))

if (city in ["New York", "San Fransisco"] and rent < 4000 ):
    print(f"You can live in {city} whith this {rent} rent.")

elif city == "Washington":
    print(f"You can't live in {city} whith this {rent} rent.")

elif city == "Chicago":
    print(f"You can live in {city} whith this {rent} rent.")

elif rent <= 3000:
    print(f"You can live in {city} whith this {rent} rent.")

else:
    print(f"You can't live in {city} whith this {rent} rent.")
