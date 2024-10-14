town = input("Melyik városban található az albérlet?")
price = int(input("Mennyibe kerül az albérlet havonta?"))

if town in ["New york", "San Francisco"] and price < 4000:
    ok = True
elif town == "Washington":
    ok = False
elif town == "Chicago":
    ok = True
elif price <= 3000:
    ok = True
else:
    ok = False

print(f"A megadott feltételekkel {"elfogadható az albérlet "+town+ " városban, ára " +str(price)+ " USD havonta!" if ok else "nem megfelelő az albérlet!"} ")