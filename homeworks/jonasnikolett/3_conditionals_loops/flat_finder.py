"""
Feladat 1: Hétköznapi nyelven leírt szöveg konvertálása Python kód-ra (if-elif-else, operátorok)
Hozz létre egy flat_finder.py nevű file-t, és kódold le a következő feladat megoldását:
A feladat célja, hogy elsajátítsd azt a képességet hogy hétköznapi módon megfogalmazott feladatokat fordítasz le python-ra.
Sarah-nak kell segítened a lakáskeresésben, a következőket tudjuk:
    Nagyon szereti New York-ot és San Fransisco-t, bármelyik városban kivenne egy lakást, ha az albérlet ára kevesebb mint 4000 USD havonta.
    Gyűlöli Washington-t, és semmi pénzért nem lakna ott
    Annyira imádja Chicago-t, hogy még a pénz sem akadály, bármit megadna azért hogy ott lakhasson
    Ha bármilyen más helyről van szó, 3000 USD vagy ez alatti havi lakbér ellenében költözne oda.
Írj egy programot, amely bekéri a felhasználótól a várost és a lakbér árát.
Ezután a fentiek alapján printeld ki egy f-string használatával hogy az adott feltételek (város és albérlet ára) mellett be tudna e költözni az adott helyre.
"""

# Város megadása
#rental_city = ("Washington", "Chicago")

while True:
    rental_city = input( "Sarah: In which city do you offer your flat for rented?")

# ha Washington SOHA
    if rental_city == "Washington":
        print(f"Agent: The city is {rental_city}.")
        print(f"Sarah: Sorry, but I really don't like {rental_city}. No way!")
        continue

# ha Chicago nincs anyagi akadály
 
    elif rental_city == "Chicago":
            print(f"Agent: The city is {rental_city}.")
            print(f"Sarah: My favorite place is {rental_city}, I'll take it!")
            

 
# ha New York és San Fransisco, kevesebb mint 4000 USD
# minden más 3000 USD
    else:
        apartment_rent_price = int(input(f"Sarah: Thank you the city information, and how much is the rent for the apartment in dollars? "))
        print(f"Agent: So, this apartment in {rental_city} is {apartment_rent_price} dollars.")

        if rental_city == "New York" or rental_city == "San Francisco":
            if apartment_rent_price < 4000:
                 print(f"Sarah: Perfect! I love {rental_city}, and the price is good for me. I'll take it!")
            else:
                print(f"Sarah: Sorry, I love {rental_city}, but the flat is expensive for me!")
                print( rental_city = input(f"Sarah: Do you have any other apartment in other city?"))
        else:
            if apartment_rent_price <= 3000:
                print(f"Sarah: Perfect! I love {rental_city}, and the price is good for me. I'll take it!")
            else:
                print(f"Sarah: Sorry, I love {rental_city}, but the flat is expensive for me!")
                print( rental_city = input(f"Sarah: Do you have any other apartment in other city?"))
    break