"""
A feladat célja, hogy elsajátítsd azt a képességet hogy hétköznapi módon megfogalmazott feladatokat fordítasz le python-ra. 
Sarah-nak kell segítened a lakáskeresésben, a következőket tudjuk:
    - Nagyon szereti New York-ot és San Fransisco-t, bármelyik városban kivenne egy lakást, ha az albérlet ára kevesebb mint 4000 USD havonta.
    - Gyűlöli Washington-t, és semmi pénzért nem lakna ott
    - Annyira imádja Chicago-t, hogy még a pénz sem akadály, bármit megadna azért hogy ott lakhasson
    - Ha bármilyen más helyről van szó, 3000 USD vagy ez alatti havi lakbér ellenében költözne oda.
Írj egy programot, amely bekéri a felhasználótól a várost és a lakbér árát. Ezután a fentiek alapján printeld ki egy f-string használatával,
hogy az adott feltételek (város és albérlet ára) mellett be tudna e költözni az adott helyre.
"""

print("Hello, help Sarah find the right apartment for her.")
name_of_city = input("In which city is the apartment located? ").capitalize()
name_of_city_var = name_of_city.strip().upper()
apartment_price = int(input("what is the price of the apartment? "))


if name_of_city_var == "CHICAGO" or apartment_price <= 3000:
   ans ="wants"
elif name_of_city_var == "NEWYORK" or "SANFRANCISCO" and apartment_price <= 4000:
     ans ="wants"
elif name_of_city_var == "WASHINGTON":
     ans = "does not want"
else:
     ans = "does not want"

print(f"Sarah looked at the apartment you recommended with location {name_of_city} and price {apartment_price} USD.She {ans} to this apartman!")