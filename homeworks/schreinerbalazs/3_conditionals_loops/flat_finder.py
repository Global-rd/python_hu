city = input("Melyik városba költöznél? ").strip()

# Ha a város Washington, azonnal kiírjuk, hogy nem költözne oda
if city.lower() == "washington":
    print(f"Sarah inkább az utcán lakik de {city}-ba nem költözik!")
else:
    # Ha nem Washington, bekérjük a lakbér árát
    rent = float(input("Mennyi a havi lakbér (USD)? "))

    # Feltételek ellenőrzése
    if city.lower() == "new york" or city.lower() == "san francisco":
        if rent < 4000:
            print(f"Sarah imádja {city} városát, a bérleti díj pedig megfelelő, mert csak USD{rent}.")
        else:
            print(f"Sarah imádja {city} városát, de a(z) USD{rent} lakbér túl magas.")
    elif city.lower() == "chicago":
        print(f"Sarah kedvenc városa {city}. Inkább nem eszik, de kifizeti valahogy a(z) {rent} Dolláros lakbért.")
    else:
        if rent <= 3000:
            print(f"Sarah szereti {city} városát, és a(z)  {rent} Dolláros lakbér is belefér.")
        else:
            print(f"Sarah szereti {city} városát, de a lakbér {rent} Dollár, ami túl magas.")