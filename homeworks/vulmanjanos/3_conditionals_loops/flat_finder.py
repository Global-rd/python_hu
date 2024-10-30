city_name = input("Please choose as city where you would live:")
flat_price = int(input("Please fill the field with monthly renting cost you would pay:"))

# if-elif-else definiálás városokra és költségre
if (city_name == "New York" or city_name == "San Fransisco") and flat_price <= 4000:
    condition = True
elif city_name == "Washington":
    condition = False
elif city_name == "Chicago":
    condition = True
elif flat_price <= 3000:
    condition = True
else:
    condition = False
    # szövegezés a válaszra
print(f"With your conditions {"flats are available for you for a price of " + str(flat_price) + " USD per month in " + city_name+ "." if condition else "we cannot offer you any flat, in " + city_name + ", sorry!"} ")
