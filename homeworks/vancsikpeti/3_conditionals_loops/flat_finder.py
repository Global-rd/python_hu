import geonamescache # Annak eldöntésére, hogy a bevitt adat város-e?
gc = geonamescache.GeonamesCache()

def enter_city(city_name=""):
    city_name = input("In which city do you offer flat? (name of city) ")
    return city_name

def city_is_real(city_name):
    # A geonamescache pack a leírás szerint erre a metódusra dictionary-t ad vissza de a type() szerint list ezért:
    city_is_real = True if len(gc.search_cities(city_name,case_sensitive=False,contains_search=True)) > 0 else False
    return city_is_real

sarah_cities = ["Chicago", "New York", "San Fransisco", "Wasington"]

city = ""
flat_price = int()

while True:
    city = enter_city(city)
    if city_is_real(city)==False:
        print(f"{city} is not an exist city.")
    else: break

flat_price = int(input("How many costs the flat? (in USD/month) "))

if city in sarah_cities:   
    if city == "Chicago":
        print(f"I love {city}. and {flat_price} USD is right for me.")
    elif city == "New York" or city == "San Fransisco":
        if flat_price < 4000:
            print(f"I like {city} and {flat_price} USD is right for me.")
        else: print(f"Sorry, the flat costs me too much.")    
    elif city == "Washington":
        print(f"Sorry, I hate this city")
else:
    print(f"I can move into {city} if the flat is cheaper than 3000 USD")

"""
Feladat 1.
Sarah
- Nagyon szereti New York-ot és San Fransisco-t, bármelyik városban kivenne egy lakást, ha az albérlet ára kevesebb mint 4000 USD havonta.
- Gyűlöli Washington-t, és semmi pénzért nem lakna ott
- Annyira imádja Chicago-t, hogy még a pénz sem akadály, bármit megadna azért hogy ott lakhasson
Ha bármilyen más helyről van szó, 3000 USD vagy ez alatti havi lakbér ellenében költözne oda.
Írj egy programot, amely bekéri a felhasználótól a várost és a lakbér árát. Ezután a fentiek alapján printeld ki egy f-string használatával hogy az adott feltételek (város és albérlet ára) mellett be tudna e költözni az adott helyre.
"""