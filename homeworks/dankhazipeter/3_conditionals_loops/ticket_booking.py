# ANSI escape kódok a színezéshez és vastagításhoz.
# Bár nem kérte a feladat, de gondoltam, hogy színes kiírással szebb lesz a program.
BOLD = '\033[1m'
BLUE = '\033[94m'
RESET = '\033[0m'


def print_seats(seats):
    print(f"{BOLD}{BLUE}  1 2 3 4 5{RESET}")  # Oszlop számok
    for i, row in enumerate(seats, 1):
        print(f"{BOLD}{BLUE}{i}{RESET} {' '.join(str(seat) for seat in row)}")
    print()


def is_valid_seat(row, col, seats):
    return 1 <= row <= len(seats) and 1 <= col <= len(seats[0]) and seats[row-1][col-1] == 0


# Filmek listája
movies = ["The Matrix", "The Matrix Reloaded",
          "The Matrix Revolutions", "Oldboy", "25th Hour"]

# Film kiválasztása
while True:
    selected_movie = input(
        "Kérem, adja meg a film nevét, amire jegyet szeretne foglalni: ")
    if selected_movie in movies:
        break
    print("Sajnos ezt a filmet nem játsszuk. Kérem, válasszon a következő filmek közül:")
    print(", ".join(movies))

# Ülések inicializálása
# Azt láttam egy leírásban, hogy Python ajánlás, hogy _ változónevekkel jelezzük, hogy az adott változót nem használjuk.
seats = [[0 for _ in range(5)] for _ in range(5)]

print(f"\nHelyek a(z) {selected_movie} című filmhez:")
print_seats(seats)

# Jegyfoglalás
while True:
    try:
        num_tickets = int(
            input("Hány jegyet szeretne foglalni? (1-25 között) "))
        if 1 <= num_tickets <= 25:
            break
        else:
            print("Kérem, 1 és 25 közötti számot adjon meg!")
    except ValueError:
        print("Kérem, egy érvényes számot adjon meg!")

booked_seats = []

for i in range(num_tickets):
    while True:
        try:
            row = int(input(f"Kérem, adja meg a {i+1}. jegy sorát (1-5): "))
            col = int(input(f"Kérem, adja meg a {i+1}. jegy oszlopát (1-5): "))

            if is_valid_seat(row, col, seats):
                seats[row-1][col-1] = 1
                booked_seats.append((row, col))
                break
            else:
                print("Érvénytelen vagy már foglalt hely. Kérem, próbálja újra.")
        except ValueError:
            print("Kérem, egy érvényes számot adjon meg!")

    print(f"\nAktuális foglalási állapot a(z) {selected_movie} című filmhez:")
    print_seats(seats)

# Foglalás összegzése
print("\nFoglalás összegzése:")
print(f"Film: {selected_movie}")
print(f"Foglalt jegyek száma: {len(booked_seats)}")
print("Foglalt helyek:")
for seat in booked_seats:
    print(f"Sor: {seat[0]}, Oszlop: {seat[1]}")
