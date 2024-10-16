from os import system
import time

system("cls")

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
    ticket_row = int(input(f"Enter a row number (0-4) for {ticket+1} ticket:"))
    ticket_column = int(input(f"Enter a column number (0-4) for {ticket+1} ticket."))

    if seating_chart[ticket_row][ticket_column] == 0:
        print(f"Your seat in {ticket_row} row {ticket_column} column is booked.")
        seating_chart[ticket_row][ticket_column] = 1
        ticket += 1
        print("Current seating arrangement")
        for row in seating_chart:
            print(row)
    else:
        print(
            f"This seat in row {ticket_row} is not available. Please choose another seat!"
        )

print("Summary of your booked tickets: ")
for seat_row in range(5):
    for seat_column in range(5):
        if seating_chart[seat_row][seat_column] == 1:
            print(f"Seat at row {seat_row}, column {seat_column} is booked.")
print(f"Thank you for booking to see {film_title}!")
