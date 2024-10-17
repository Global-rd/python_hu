""" Feladat 1: Hétköznapi nyelven leírt szöveg konvertálása Python kód-ra (if-elif-else, operátorok)
- Hozz létre egy flat_finder.py nevű file-t, és kódold le a következő feladat megoldását:
- A feladat célja, hogy elsajátítsd azt a képességet hogy hétköznapi módon megfogalmazott feladatokat fordítasz le python-ra.
- Sarah-nak kell segítened a lakáskeresésben, a következőket tudjuk:
    > Nagyon szereti New York-ot és San Fransisco-t, bármelyik városban kivenne egy lakást, ha az albérlet ára kevesebb mint 4000 USD havonta.
    > Gyűlöli Washington-t, és semmi pénzért nem lakna ott
    > Annyira imádja Chicago-t, hogy még a pénz sem akadály, bármit megadna azért hogy ott lakhasson
    - Ha bármilyen más helyről van szó, 3000 USD vagy ez alatti havi lakbér ellenében költözne oda.
- Írj egy programot, amely bekéri a felhasználótól a várost és a lakbér árát. Ezután a fentiek alapján printeld ki egy f-string használatával hogy az adott feltételek (város és albérlet ára) mellett be tudna e költözni az adott helyre.
"""

print("Help Sarah finding a flat in a city she likes, for a rate she can afford.")
input("Press Enter if you're ready to go!")

# A külső while ciklus az újbóli lekérdezés indítására kérdez rá, a lefutás végén:
while True:
    # Belső while ciklus, a tartalmi város/lakbér opciók vizsgálatára:
    while True:
        city = input("Which city is the flat in? ").strip().title()
        if city == "Washington":
            print(f"Let's stop here. {city} is the only place Sarah doesn't want to live in at any cost. Please start over and choose another city.")
            continue
        
        rental_rate = int(input("What is the rental rate per month in USD? "))

        print(f"The city and rental rate you have choosen: {city} for {rental_rate} USD per month.\nKnowing Sarah's preferences here is the deal:\n")

        if ( city in ["New York", "San Fransisco"] and rental_rate < 4000 ) or city == "Chicago" or rental_rate < 3000:
            print(f"OK! This is a good place for her in {city} for {rental_rate} USD.")
            break
        else:
            print(f"This city-rental rate combo ({city}-{rental_rate} USD) does not meet Sarah's requirements.\nPlease choose another city and rental rate.")

 # A külső while ciklus végén rákérdezés, hogy akarunk-e új város/költség opciót megvizsgálni:   
    new_query = input("Do you want to start over with a new query? (Y/N) ")
    if new_query.capitalize() != "Y":
        break