import pprint

#Aktuális mozifilmek
movie_films = {
    "Back to the Future" :[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]],
    "Home Alone" :[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]],
    "Jurassic Park" :[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]],
    "Paul" :[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
}

# Bekérjük melyik filmre szeretne jegyet venni
while True:
    choosen_movie = input(f"Please choose a movie from the list {list(movie_films.keys())}: ")
    if choosen_movie in movie_films.keys():
        print(f"You have selected {choosen_movie}!")
        break
    else:
        print("Sorry, that movie is not available")


# Megmutatjuk a moziterem foglaltságát
print("\nCurrent seat arrangement at your choosen movie:")
for row in movie_films[choosen_movie]:
    print(" ".join(str(seat) for seat in row))

#Bekérjük hány jegyet akar foglalni

available_seats = sum(available_seat == 0 for row in movie_films[choosen_movie] for available_seat in row)


while True:
    reserved_seat_number = int(input("\nHow many ticket would you like to book?: "))
    if reserved_seat_number >= available_seats:
        print("There is not enough available seat.")
    else:
        break

  
#Bekérjük a pontos helyét a jegyeknek
for ticket_number in range(reserved_seat_number):
    print(f"\nBooking ticket {ticket_number+1}...")
    while True:
        row_number_pre = int(input("Enter the row number (1-5): "))
        row_number = row_number_pre - 1
        column_number_pre = int(input("Enter the column number (1-5): "))
        column_number = column_number_pre - 1

        if row_number_pre > 5 or row_number_pre < 1 or column_number_pre > 5 or column_number_pre < 1:
            print("\nThere is no seat in this number! Try again: ")
            continue
       
        elif (movie_films[choosen_movie])[row_number][column_number] != 0:
            print("\nThis seat is unavailable!")
            continue

        else:
            (movie_films[choosen_movie])[row_number][column_number] = 1
            break
    print(f"\nCurrent Seating Arrangement: ")
    for row in movie_films[choosen_movie]:
        print(" ".join(str(seat) for seat in row))

print("\nSummary of your tickets:")
print(f"\nYou have {reserved_seat_number} booked seats:")

for row_index, row in enumerate(movie_films[choosen_movie]):
    for col_index, seat in enumerate(row):
        if seat == 1:
            print(f"Seat at Row: {row_index + 1}, Column: {col_index + 1}")





