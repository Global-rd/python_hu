"""
Ebben a házi feladatban egy mozi helyfoglaló rendszerének egy egyszerűsített változatát kell lefejlesztened. 
A fehasználónak képesnek kell lennie kiválasztani melyik filmre szeretne helyet (vagy helyeket) foglalni. 
Egy 5x5-ös mátrixban (list of lists) látnia kell mely helyek szabadok, és ezekből le kell tudnia foglalni azt a jegy mennyiséget amennyit szeretne. 
A feladathoz segítséget nyújtanak a következő pontok:
    - Készíts egy tetszőleges listát a kedvenc filmjeiddel. -- kész
    - Ezután kérd be a felhasználótól a film nevét amire szeretne jegy(eket) foglalni. -- kész
      Amennyiben a film nincs a listádban, addig kérdezd a felhasználót amíg egy olyan filmet nem választ ami szerepel az előre definiált filmek között. -- kész
    - Készíts egy 2 dimenziós listát (list of lists) amely 5 sort és 5 oszlopot reprezentál.Állítsd minden értéket 0-ra, ezek fogják a szabad helyeket jelenteni. -- kész
    - Használj egy nested for loopot hogy ezt ki is printeld a felhasználónak. -- kész
    - Kérdezd meg a felhasználót, hogy hány jegyet szeretne vásárolni. -- kész
    - Ezután minden jegynek a sor és oszlopszámát kérd be tőle. Amennyiben ez egy valid oszlop és sor szám (nem kisebb vagy nagyobb mint az elérhető számok, és nem foglalt még a hely),
      tárold el a foglalást, és frissítsd a terminálban az üléseket (printeld ki minden iterációban amikor egy foglalás megtörténik). Kerüljön 1-es a lefoglalt helyre.
    - Biztosítsd, hogy nem foglal több jegyet a felhasználó mint amennyit eredetileg kért.
Ha végzett, printelj ki egy összegzést a lefoglalt jegyekről.
"""

movies_list = ["Die Hard 3", "Pulp Fiction", "Life Of Brian", "The Holy Grail"]
var_movies_list =[x.lower() for x in movies_list]

print(f"Welcome,today's movie choices {movies_list}")
      
while True:
    movie_title = input("Which movie would you like to choose? ").lower()
    if movie_title in var_movies_list:
        break
    else:
        print ("Wrong title, try again.")

def print_cinema_hall(cinema_hall):
    print(f"- {movie_title} -")
    for row in cinema_hall:
        print(row)

rows, cols = 5, 5
cinema_hall = [[0 for _ in range(cols)] for _ in range(rows)]
print_cinema_hall(cinema_hall)

while True:
    ticket = int(input("How many tiket do you want? "))
    if ticket <= rows * cols:
        break
    else:
        print ("Unfortunately, there is not enough space in the hall")

attempts = 0
while attempts < ticket:
    hall_rows = int(input("Please indicate which row you choose: (0 - 4) "))
    hall_cols = int(input("Please indicate which column you choose: (0 - 4) "))
    if 0 <= hall_rows < rows and 0 <= hall_cols < cols:
       attempts += 1
       if cinema_hall[hall_rows][hall_cols] != 0:
          attempts -= 1
          print("Reserved!")
       else:
          cinema_hall[hall_rows][hall_cols] = 1
          print_cinema_hall(cinema_hall)
          continue      
    else:
      print("Please write the good row/column pair!")
else:
    print_cinema_hall(cinema_hall)
