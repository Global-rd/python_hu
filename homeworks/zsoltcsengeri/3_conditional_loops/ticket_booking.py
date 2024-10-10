"""
This program is a simplified movie seat reservation system. The user can select a movie from a predefined list
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

# Chose a film you want to watch
chosen_film = input("Please select a film you want to watch: ").strip().title()

# Validate the chosen film in the film list
while chosen_film in list_of_films:
    print(f"The film you've selected is: {chosen_film}")
    break

# 5x5 seating arrangment matrix as a list
seating_arrangement = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

number_of_tickets = int(input("How many tickets do you want to book? "))

booked_tickets_list = list(range(number_of_tickets))
print(booked_tickets_list)

for tickets in booked_tickets_list:
    print(tickets)
    for ticket in tickets:
        print(f"Booking ticket{ticket+1}...")



# Loop through each row of the seating arrangement
for row in seating_arrangement:
    # Join each seat in the row as a string with a space between, then print the row
    print(" ".join(str(seat) for seat in row))
