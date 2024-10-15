movie_theater = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

def enter_movie(movie=""):
    movies = ["Snowden", "Matrix", "Swordfish", "Imitation game", "Love actually"]
    print("Available movies: ")
    for title in movies:
        print(f" - {title}")
    while movie not in movies:
        movie = input("Which movie do you want to watch? ")
        if movie not in movies:
            print("Error message... This movie does not exists on my list.")
    return movie

def enter_row():
    row = 0
    while row > 5 or row < 1:
        row = int(input("In which row do you want to seat? (1-5)"))
        if row > 5 or row < 1: 
            print("Error message... We have only 5 row in the theater.")
    return row

def enter_seat():
    seat = 0
    while seat > 5 or seat < 1:
        seat = int(input("In which seat do you want to seat? (1-5)"))
        if seat > 5 or seat < 1:
            print("Error message... We have only 5 seat in a row.")
    return seat

def is_seat_available(row, seat):
    seat_empty = True if movie_theater[row][seat] == 0 else False
    if seat_empty==False:
        print("Error message... This seat is reserved.")
    return seat_empty

def reserved_seat_status():
    i = 0
    for row in movie_theater:
        i += 1
        print(f"{i}. row -> {row}")

movie = enter_movie()   
reserved_seat_status()
tickets = int(input("How many tickets do you want to buy? "))

reservs = 0
new_ticket_row=0
new_ticket_seat=0
while reservs < tickets:
    while True:
        new_ticket_row=enter_row()-1
        new_ticket_seat=enter_seat()-1
        if is_seat_available(new_ticket_row, new_ticket_seat):
            break
    movie_theater[new_ticket_row][new_ticket_seat] = 1
    reserved_seat_status()
    reservs += 1

"""
Készíts egy tetszőleges listát a kedvenc filmjeiddel.
Ezután kérd be a felhasználótól a film nevét amire szeretne jegy(eket) foglalni. Amennyiben a film nincs a listádban, addig kérdezd a felhasználót amíg egy olyan filmet nem választ ami szerepel az előre definiált filmek között.
Készíts egy 2 dimenziós listát (list of lists) amely 5 sort és 5 oszlopot reprezentál. Állítsd minden értéket 0-ra, ezek fogják a szabad helyeket jelenteni.
Használj egy nested for loopot hogy ezt ki is printeld a felhasználónak. 
Kérdezd meg a felhasználót, hogy hány jegyet szeretne vásárolni.
Ezután minden jegynek a sor és oszlopszámát kérd be tőle. 
Amennyiben ez egy valid oszlop és sor szám (nem kisebb vagy nagyobb mint az elérhető számok, 
és nem foglalt még a hely), tárold el a foglalást, 
és frissítsd a terminálban az üléseket (printeld ki minden iterációban amikor egy foglalás megtörténik). 
Kerüljön 1-es a lefoglalt helyre.
Biztosítsd, hogy nem foglal több jegyet a felhasználó mint amennyit eredetileg kért.
"""
