favorite_films = ["Keresztapa", "Nagymenők", "Ghostbusters", "Star Wars", "Kémek a sasfészekben", "Oroszországból szeretettel"]

while True:
    chosen_film = input("Melyik filmre szeretne jegyet venni?")
    if chosen_film in favorite_films:
        break
    else:
        print("Jelenleg ezeket a filmeket vetítjük. Kérem ezek közül válasszon:")
        for movie in favorite_films:
            print(movie)

reserved_seats_sum = 0
seats_in_the_cinema = 25

seats = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]

print("Szabad helyek a teremben:")

for rows in seats:
    print(rows)

while True:
    ticket_total = int(input("Hány jegyet szeretne vásárolni?"))

    if ticket_total == 0:
        print("Legalább 1 jegy vásárlása kötelező!")
    elif (reserved_seats_sum + ticket_total) <= seats_in_the_cinema:
        break
    else:
        print("Nincs elég hely a teremben. Kérem módosítsa a jegyek darabszámát!")


for i in range(ticket_total):
    while True:

        print("A(z) " +str(i + 1)+ ". jegy foglalása:")
        column = int(input("Melyik oszlopba szeretné kérni a(z) " +str(i + 1)+ " jegyet? (0-4)"))
        row = int(input("Melyik sorba szeretné kérni a(z) " +str(i + 1)+ " jegyet? (0-4)"))

        if 0 <= row < 5 and 0 <= column < 5 and seats[row][column] == 0:
            seats[row][column] = 1
            print("Frissített ülésrend:")
            for rows in seats:
                    print(rows)
            break
        else:
            print("Érvénytelen hely vagy már foglalt. Kérem, válasszon másikat!")

print("---xxx---xxx---xxx---xxx---xxx---xxx---xxx---xxx---")
print("Foglalás összegzése:")

for r in range(len(seats)):
    for c in range(len(seats[r])):
        if seats[r][c] == 1:
            print("Jegy foglalva a " + str(r) + " sorba, és " + str(c) + " oszlopba!")

print("Köszönjük a jegyfoglalást a " + chosen_film + " című filmre. Jó szórakozást.")