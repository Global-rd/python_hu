'''
3. házi feladat

Feladat extra: ticket_booking
egy mozi helyfoglaló rendszerének egyszerűsített változata
'''

import sys
import os
import copy # for deepcopy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../_0_Functions')))

from terminal_clearer import clear_terminal
from ticket_booking_functions import print_seating_area, update_seating_area_booked, update_seating_area_bought, book_seat

clear_terminal()

movies = [
    "A Night at the Roxbury",  
    "Dumb and Dumber",
    "The Hangover",
    "Superbad",
    "Anchorman: The Legend of Ron Burgundy",
    "Hot Fuzz",
    "Step Brothers",
    "Zoolander",
    "Monty Python and the Holy Grail",
    "Shaun of the Dead"
]

print(f"Available movies:")
for id,movie in enumerate(movies,1):
    print(f"  {id} - {movie}")

while True:
    # Ask the user for input
    selected_number = int(input("Please select a movie by its number: ").strip())

    # Check if the movie is on the list
    if 1 <= selected_number <= len(movies):
        selected_movie = movies[selected_number - 1]
        break
    else:
        print(f"Please enter a number between 1 and {len(movies)}.")
clear_terminal()

print(selected_movie)

seating_area = [
    [0, 0, 0, 0, 0],  
    [0, 0, 1, 1, 1], 
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1]
]





print_seating_area(seating_area)

# Ask the user for input
tickets_numbers = int(input("How many tickets would you like to buy? (number) ").strip())


# Ticket booking part
while True:

    temp_seating_area = copy.deepcopy(seating_area) # temporary seating area for this ciklus
    clear_terminal()

    print_seating_area(temp_seating_area)

    for i in range(1,tickets_numbers+1):
        clear_terminal()
        print_seating_area(temp_seating_area)
        book_seat(temp_seating_area, i)  # Call the book_seat function

    print_seating_area(temp_seating_area)

    accepted = str(input("Are you placing the order? (yes/no): ").strip().lower())


    if accepted == "yes":
        seating_area = temp_seating_area  # Finalize booking
        break


# update the selected seats to bought
update_seating_area_bought(seating_area)

clear_terminal()
print(f"Thank you for purchasing the tickets below:")
print_seating_area(seating_area)

input("Press Enter to continue...")

# update the selected seats to bought
update_seating_area_booked(seating_area)

clear_terminal()
print_seating_area(seating_area)



