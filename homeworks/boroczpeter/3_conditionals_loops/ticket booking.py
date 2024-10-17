import time

# defining the basic information: films and seats
films = ["Gladiator", "Aliens", "The Simpsons", "Terminator", "Taken"]
seats = [[0 for _ in range(5)] for _ in range(5)]

# check wether the film is in the given list
while True:
    film = input(f"Choose a film from the list: {', '.join(films)}: ").strip() # case sensitive
    if film in films:
        break
    else:
        print("This film is not in the list. Please choose from the list!")

def print_seats(seats):
    print("\nFree seats:")
    for row in seats:
        print(" ".join(str(seat) for seat in row))

print_seats(seats)

while True:
    try:
        tickets = int(input("Please enter the number of the seats you want to purchase: "))
        if tickets > 0 and tickets <= 25:
            break
        else:
            print("Oh no! You can purchase maximum 25 tickets. Enter a value between 1 and 25.")
    except ValueError:
        print("Pleae enter a valid number!")

book_seats = []
for i in range(tickets):
    while True:
        try:
            row = int(input(f"Give me the row number (1-5) a {i + 1}. for the ticket: ")) - 1
            col = int(input(f"Give me the row number (1-5) a {i + 1}. for the ticket: ")) - 1

            # check the availability of wether the seat is free or not
            if 0 <= row < 5 and 0 <= col < 5 and seats[row][col] == 0:
                seats[row][col] = 1
                book_seats.append((row + 1, col + 1))
                print(f"The {i + 1}. ticket is booked for row {row + 1}. sor, {col + 1}. coloumn.")
                print_seats(seats)
                break
            else:
                print("Error: The seat is reserved or invalid raw/column number.")
        except ValueError:
            print("Error: Type in a valid number!")

# summary
time.sleep(1)
print("\nInformation about the ticket(s) your booked:")
print(f"The choosen film is: {film}")
print(f"Booked seats are: {', '.join([f'{row}. raw, {col}. coloumn' for row, col in book_seats])}")