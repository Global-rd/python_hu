city = input("Add meg a város nevét : ")
city = city.strip().upper()
print(city)

price = int(input("Add meg a bérleti díjat :"))
print(city, price)

if (city == "NEW YORK" or "SAN FRANSISCO") and price <= 4000 :
    print(f"Sarah {city}-ben van {price} $-ért lakás vedd ki !")
elif city == "WASINGTON":
    print(f"Sarah {city} -ben lenne lakás ne béreld ki !")
elif city == "CHICAGO" :
    print(f"Sarahvan {city}-ben lakás béreld ki !")
elif price <= 3000 and city !="WASINGTON" :
    print(f"Sarah találtunk lakást {city}-ban {price} $-ért béreld ki ! ")
else: print("Sarah nem találtunk megfelelő lakást")
