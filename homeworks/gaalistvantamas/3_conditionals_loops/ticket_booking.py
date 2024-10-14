"""
Author: Gaál István Tamás
Task: Homework-3 / 3
"""

the_movies_list = ["Iron Man", "Spider-Man", "The Hulk", "The Avengers"]
seats_in_the_cinema_room = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

the_chosen_movie = input(f"Please choose a movie from the list: {
                         the_movies_list}\n").strip().title()
while not the_chosen_movie in the_movies_list:
    print("Sorry, that movie is not available.")
    the_chosen_movie = input(f"Please choose a movie from the list: {
                             the_movies_list}\n").strip().title()
print(f"You chose {the_chosen_movie} movie!")

def print_seat_arragement():
    print("\nCurrent Seating Arragment:")
    for i in range(0, 5):
        if i > 0:
            print("")
        for j in range(0, 5):
            print(seats_in_the_cinema_room[i][j], end=" ")
    print("\n")

print_seat_arragement()

tickets_booking_num = int(input("How many tickets would you like to book? "))

if tickets_booking_num < 1:
    print("Please give a number than bigger 0!")
    while tickets_booking_num <= 0:
        tickets_booking_num = int(
            input("How many tickets would you like to book?"))

# booking
for ticket_num in range(0, tickets_booking_num):
    print(f"Booking ticket {ticket_num+1}....")

    booking_row_num = int(
        input(f"Enter the row number (0-4) for ticket {ticket_num+1}: "))
    while not (booking_row_num >= 0 and booking_row_num <= 4):
        booking_row_num = int(
            input(f"Enter the row number (0-4) for ticket {ticket_num+1}: "))

    booking_column_num = int(
        input(f"Enter the column number (0-4) for ticket {ticket_num+1}: "))
    while not (booking_column_num >= 0 and booking_column_num <= 4):
        booking_column_num = int(
            input(f"Enter the column number (0-4) for ticket {ticket_num+1}: "))

    if seats_in_the_cinema_room[booking_row_num][booking_column_num] == 1:
        print("This seat is already taken, please choose another.")
        booking_row_num = int(
            input(f"Enter the row number (0-4) for ticket {ticket_num+1}: "))
        while not (booking_row_num >= 0 and booking_row_num <= 4):
            booking_row_num = int(
                input(f"Enter the row number (0-4) for ticket {ticket_num+1}: "))

        booking_column_num = int(
            input(f"Enter the column number (0-4) for ticket {ticket_num+1}: "))
        while not (booking_column_num >= 0 and booking_column_num <= 4):
            booking_column_num = int(
                input(f"Enter the column number (0-4) for ticket {ticket_num+1}: "))

    seats_in_the_cinema_room[booking_row_num][booking_column_num] = 1
    
    print_seat_arragement()
    
    if ticket_num == (tickets_booking_num - 1):
        print(f"You booked {ticket_num + 1} tickets!\n")

# Summary
print("Summary of your booked tickets:")
for i in range(0, 5):
    for j in range(0, 5):
        if seats_in_the_cinema_room[i][j] == 1:
            print(f"Seat at row {i}, column {j} is booked.")

print(f"\nThank you for booking tickets to see {the_chosen_movie}!\n")
