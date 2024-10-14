from os import system

# from pprint import pprint
import time

system("cls")
"""
Booking ticket 1.
Enter a row number (0-4) for ticket 1
Enter a column number for ticket 1
Print current seat arrangement
Booking ticket 2.
Enter a row number (0-4) for ticket 2
Enter a column number (0-4) for ticket 2
Print current seat arrangement
"""

film_selection = ["Constantine", "Hidden Figures", "Tango and Cash", "The Rock"]
ticket = 0
seating_chart = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

film_title = input(
    "Please select a film from the list: Constantine, Hidden Figures, Tango and Cash, The Rock: "
)
while True:
    if film_title in film_selection:
        print(f"You have selected {film_title}!")
        break
    else:
        print("Sorry, this film is not available!")
        film_title = input(
            "Please select a film from the list: Constantine, Hidden Figures, Tango and Cash, The Rock: "
        )

number_of_tickets = int(input("How many tickets would you like to book?: "))
print("Current seating arrangement")
for row in seating_chart:
    print(row)

while number_of_tickets > ticket:
    print(f"Booking {ticket+1}...")
    time.sleep(1)
    while True:
        ticket_row = int(input(f"Enter a row number (0-4) for {ticket+1} ticket:"))
        ticket_column = int(
            input(f"Enter a column number (0-4) for {ticket+1} ticket.")
        )
        break
    ticket_matrix = [ticket_row, ticket_column]
    # eddig mukodik

    if ticket_matrix[:2] in seating_chart == 0:
        print(f"Your seat in {ticket_row}row {ticket_column} column is booked.")
        break
    else:
        print(
            f"This seat in row {ticket_row} is not available. Please choose another seat!"
        )
        break


"""for ticket_row in seating_chart:  # Harom indexig irja ki 0, 1,2,
    for ticket_column in range(2):  # 2 indexig irja 0,1
        print(i, j)
for ticket_row in seating_chart:
    print(f"You have selected row {ticket_row}")
for ticket_column in seating_chart:
    print(f"You have selected column {ticket_column}")
"""
