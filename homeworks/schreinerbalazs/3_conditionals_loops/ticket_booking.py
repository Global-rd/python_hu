# Kedvenc filmek listája
movies = ["MAD MAX", "ÜVEGTIGRIS", "FEKETE PONT", "BRIAN ÉLETE", "BRONXI MESE"]

# 5x5-ös ülésmátrix létrehozása, minden hely kezdetben 0 (szabad)
seats = [[0 for _ in range(5)] for _ in range(5)]

# Film kiválasztása
def select_movie():
    while True:
        movie_choice = input("\nA fenti filmek közül melyikre szeretnél jegyet foglalni? ").strip().upper()
        if movie_choice in movies:
            print(f"\n{movie_choice}? Mi is imádjuk, és pont játsszuk.")
            return movie_choice
        else:
            print("\nA fenti listából válassz!")

# Ülőhelyek megjelenítése
def display_seats():
    print("\nMoziterem ülései (0 = szabad, F = foglalt):")
    for row in seats:
        print(" ".join(str(seat) for seat in row))

# Foglalás
def book_seats(num_tickets):
    booked_seats = []
    for _ in range(num_tickets):
        while True:
            try:
                row = int(input("\nMelyik sor? (1-5): ")) - 1  # 0-4 helyett 1-5 indexelés
                col = int(input("\nHányas szék? (1-5): ")) - 1  # 0-4 helyett 1-5 indexelés
                
                # Ellenőrizzük, hogy a megadott sor és oszlop érvényes-e
                if row < 0 or row >= 5 or col < 0 or col >= 5:
                    print("\nIlyen hely nincs. Válassz létező helyet!")
                    continue

                # Ellenőrizzük, hogy a hely foglalt-e
                if seats[row][col] == "F":
                    print("\nMások ölébe nem ülhetsz! Válassz másik helyet!")
                else:
                    # Foglalás végrehajtása
                    seats[row][col] = "F"  # Lefoglalt hely "F" jelöléssel így jobban átlátom
                    booked_seats.append((row + 1, col + 1))  # A visszatérő érték legyen 1-től 5-ig
                    display_seats()  # Frissített ülésrendszer kiírása
                    break
            except ValueError:
                print("\n►Hiba: Kérlek adj meg 1-5-ig számot a sor és oszlop megadásánál.")

    return booked_seats

# Program kezdete
def main():
    print("\nÖrülök, hogy itt vagy! Válassz egyet a kiváló filmek közül:")
    print("\n".join(movies))
    
    selected_movie = select_movie()  # Felhasználó filmválasztása
    display_seats()  # Kiírjuk az üres üléseket

    # Bekérjük, hány jegyet szeretne foglalni
    while True:
        try:
            num_tickets = int(input("\nHányan jöttök? (Max. 25 hely van.)"))
            if num_tickets > 0 and num_tickets <= 25:
                break
            else:
                print("\nMaximum 25-en fértek el, és egynél kevesebben nem tudsz jönni.")
        except ValueError:
            print("\nSzámot adj meg 1-25 között!")

    booked_seats = book_seats(num_tickets)  # Jegyfoglalás

    # Foglalás összegzése 
    print(f"\nVálasztott film: {selected_movie}")
    print("Lefoglalt ülés(ek):")
    for seat in booked_seats:
        print(f"{seat[0]}. sor ► {seat[1]}. szék")

# Program futtatása
if __name__ == "__main__":
    main()