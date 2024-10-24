"""
This program is a simplified movie seat reservation system. The user can select a movie from a predefined list(from wikipedia)
and choose available seats in a 5x5 seating grid (represented as a list of lists). The program guides the user 
through the following steps:

1. A list of favorite movies is presented.
2. The user is prompted to select a movie. If the movie is not in the list, they are asked again until a valid movie is chosen.
3. A 5x5 seating arrangement is displayed, with all seats initially set to 0 (available).
4. The user is asked how many tickets they want to reserve.
5. For each ticket, the user provides a row and column number for the desired seat.
6. The program checks if the seat is available and within the valid range.
7. Reserved seats are marked with a 1, and the seating arrangement is updated after each reservation.
8. The program ensures the user does not reserve more seats than they initially requested.
"""

# List of films
list_of_films = [
    "Avatar",
    "Avengers: Endgame",
    "Avatar: The Way of Water",
    "Titanic",
    "Star Wars: The Force Awakens",
    "Avengers: Infinity War",
    "Spider-Man: No Way Home",
    "Inside Out 2",
    "Jurassic World",
    "The Lion King",
    "The Avengers",
    "Furious 7",
    "Top Gun: Maverick",
    "Frozen II",
    "Barbie",
    "Avengers: Age of Ultron",
    "The Super Mario Bros. Movie",
    "Black Panther",
    "Harry Potter and the Deathly Hallows – Part 2",
    "Star Wars: The Last Jedi",
    "Deadpool & Wolverine",
    "Jurassic World: Fallen Kingdom",
    "Frozen",
    "Beauty and the Beast",
    "Incredibles 2",
    "The Fate of the Furious",
    "Iron Man 3",
    "Minions",
    "Captain America: Civil War",
    "Aquaman",
    "The Lord of the Rings: The Return of the King",
    "Spider-Man: Far From Home",
    "Captain Marvel",
    "Transformers: Dark of the Moon",
    "Skyfall",
    "Transformers: Age of Extinction",
    "The Dark Knight Rises",
    "Joker",
    "Star Wars: The Rise of Skywalker",
    "Toy Story 4",
    "Toy Story 3",
    "Pirates of the Caribbean: Dead Man's Chest",
    "Rogue One: A Star Wars Story",
    "Aladdin",
    "Star Wars: Episode I – The Phantom Menace",
    "Pirates of the Caribbean: On Stranger Tides",
    "Jurassic Park",
    "Despicable Me 3",
    "Finding Dory",
    "Alice in Wonderland",
]

# Prompt user to choose a film
chosen_film = input("Please select a film you want to watch: ").strip().title()

# Validate movie selection until a valid movie is selected
while chosen_film not in list_of_films:
    print("\nSorry, that movie is not available.")
    chosen_film = input("Please select a film from the list: ").strip().title()
print(f"\nYou have selected {chosen_film}!")

# 5x5 seating arrangement matrix as a list
seating_arrangement = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

print("\nThese are the seats you can choose: ")

# Loop through each row of the seating arrangement to display the seats
for row in seating_arrangement:
    # Join each seat in the row as a string with a space between, then print the row
    print(" ".join(str(seat) for seat in row))

# Ask how many tickets the user wants to book
number_of_tickets = int(input("\nHow many tickets do you want to book? "))

# Loop to book each ticket
booked_seats = [] # Initialize an empty list to store booked seats

for ticket in range(number_of_tickets):
    print(
        f"\nBooking ticket {ticket + 1}..."
    )  # Display ticket number to user (ticket is a zero-based index so add 1 to display Booking ticket 1 when ticket =0 and so on)

    # Keep asking for a valid seat (not already reserved)
    while True:
        # Get row and column for the ticket
        row = int(input(f"Enter the row number (0-4) for ticket {ticket + 1}: "))
        column = int(input(f"Enter the column number (0-4) for ticket {ticket + 1}: "))
        
        # Check if the seat is already booked
        if seating_arrangement[row][column] == 1:
            print(
                "\nSorry, but this seat has already been reserved. Please choose another seat."
            )
        else:
            # If the seat is available, mark it as booked and break out of the loop
            seating_arrangement[row][column] = 1
            booked_seats.append((row, column)) # Append the row and column as a tuple
            break

    # Show the updated seating arrangement after each booking
    print("\nUpdated Seating Arrangement:")
    for row in seating_arrangement:
        print(" ".join(str(seat) for seat in row))

# Booking summary
print("\nBooking Summary:")
for seat in booked_seats:
    row, column = seat  # Unpack the row and column from the tuple
    print(f"Seat booked at row {row}, column {column}")
print(f"\nThank you for booking tickets to watch {chosen_film}!")

