"""
This is a rock, paper, scissors game.
You can determine at the beginning of the game how many sets you want to play.
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

# Initialise the starting point from where the number of sets and scores are counted.
current_set = 0
player_1_scores = 0
player_2_scores = 0

# While loop for iterating the game until we reach the number of sets
while current_set < number_of_sets:
    print(f"The current set is: {current_set + 1}")

    player_1 = input(
        "Player One: What's your choice mate? rock, paper, scissors?").strip().lower()

    if player_1 in answers:
        print(f"Player One:{player_1}")

    else:
        print(
            f"{player_1} is not a valid choice, please make your choice from rock, paper, scissors words"
        )
        player_1 = input(
            "Player One: What's your choice mate? rock, paper, scissors?").strip().lower()

    player_2 = input("Player Two: What's your choice mate? rock, paper, scissors?").strip().lower(
    )

    if player_2 in answers:
        print(f"Player Two:{player_2}")

    else:
        print(
            f"{player_2} is not a valid choice, please make your choice from rock, paper, scissors words"
        )
        player_2 = input(
            "Player One: What's your choice mate? rock, paper, scissors?").strip().lower()


# Compare the players' answers

    if player_1 == player_2:
        print("Draw")

    elif player_1 == "rock" and player_2 == "paper":
        print("Player Two won")

    elif player_1 == "paper" and player_2 == "scissors":
        print("Player Two won")

    elif player_1 == "scissors" and player_2 == "rock":
        print("Player Two won")
        player_2_scores += 1

    else:
        print("Player One won")
        player_1_scores += 1

    current_set += 1

# Announcing the winner
print(f"The scores are Player One: {
      player_1_scores} and Player Two: {player_2_scores}")
if player_1_scores > player_2_scores:
    print("The winner is Player One!")
elif player_1_scores == player_2_scores:
    print("No winner, this is draw!")
else:
    print("The winner is Player Two!")
