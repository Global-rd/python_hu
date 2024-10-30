"""
flat_finder.py --- Asztalos Lajos --- 2024.10.12
"""
#Input
city = input("Város:").strip().title()
apartment_rent = int(input("Bérleti díj dollárban:"))
#Conditional
if city == "Washington":
    print(f"Washingtonba {apartment_rent} dollár bérleti díjjért sem költözhetsz, mert utálod ezt a várost")
elif (city in ['New York','San Francisco'] and apartment_rent < 4000) or apartment_rent <=3000 or city == "Chicago":
    print(f"Beköltözhetsz a {city}i lakásba {apartment_rent} dollár bérleti díjjért")
else:
    print(f"Nem költözhetsz a {city}i lakásba {apartment_rent} dollár bérleti díjjért, mert meghaladja a keretedet")