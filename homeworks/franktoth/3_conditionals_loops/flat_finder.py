
"""Sarah-nak kell segítened a lakáskeresésben, a következőket tudjuk:
- Nagyon szereti New York-ot és San Fransisco-t, bármelyik városban kivenne egy lakást, ha az albérlet ára kevesebb mint 4000 USD havonta.
- Gyűlöli Washington-t, és semmi pénzért nem lakna ott
- Annyira imádja Chicago-t, hogy még a pénz sem akadály, bármit megadna azért hogy ott lakhasson
- Ha bármilyen más helyről van szó, 3000 USD vagy ez alatti havi lakbér ellenében költözne oda.
Írj egy programot, amely bekéri a felhasználótól a várost és a lakbér árát. Ezután a fentiek alapján printeld ki egy f-string használatával hogy az adott feltételek (város és albérlet ára) mellett be tudna e költözni az adott helyre.
"""


city = input("Enter the city: ")
rent = int(input("Enter the monthly rent in USD: "))

if city == "New York" or city == "San Francisco":
  if rent <= 4000:
    print(f"Sarah would love to move to {city} for ${rent}!")
  else:
    print(f"Sarah would like to move to {city}, but the rent is too high.")
elif city == "Washington":
  print(f"Sarah would never move to {city}!")
elif city == "Chicago":
  print(f"Sarah would love to move to {city}!")
else:
  if rent <= 3000:
    print(f"Sarah would consider moving to {city} for ${rent}.")
  else:
    print(f"Sarah would not move to {city} due to the high rent.")