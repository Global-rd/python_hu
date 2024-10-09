"""
This is a rock, paper, scissors game.
You can detremine at the begining of the game how many sets you want to play.
"""

# The wellknown 3 answers are stored in a tuple
answers = ("rock", "paper", "scissors")

# Ask for the number of sets the users want to play
number_of_sets = int(
    input("Guys, how many sets do you want to play in a game? "))

while True:
    if number_of_sets % 2 == 0:

        print(
            f"{number_of_sets} is even, therefore we can play draw. Please give me an odd number"
        )
        number_of_sets = int(
            input("Guys, how many sets do you want to play in a game? "))

    else:
        print(f"The game will consist of {number_of_sets} sets")
        break

player_1 = input(
    "What's your choice mate? rock, paper, scissors?").strip().lower()
while True:
    if player_1 in answers:
        print(f"Player One:{player_1}")
        break
    else:
        print(
            f"{player_1} is not a valid choice, please make your choice from rock, paper, scissors words"
        )
        player_1 = input(
            "What's your choice mate? rock, paper, scissors?").strip().lower()


player_2 = input("What's your choice mate2? rock, paper, scissors?").strip().lower(
)
while True:
    if player_2 in answers:
        print(f"Player Two:{player_2}")
        break
    else:
        print(
            f"{player_2} is not a valid choice, please make your choice from rock, paper, scissors words"
        )
        player_2 = input(
            "What's your choice mate2? rock, paper, scissors?").strip().lower()
