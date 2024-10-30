"""
This is a rock, paper, scissors game.
You can decide at the start how many rounds you'd like to play.
"""

# The well-known 3 options are stored in a tuple
answers = ("rock", "paper", "scissors")

# Ask for the number of rounds the players want to play
number_of_rounds = int(
    input("How many rounds do you want to play? "))

while True:
    if number_of_rounds % 2 == 0:

        print(
            f"{number_of_rounds} is even, so we could end in a draw. Please enter an odd number"
        )
        number_of_rounds = int(
            input("How many rounds do you want to play in a game? "))

    else:
        print(f"The game will consist of {number_of_rounds} rounds")
        break

# Initialise the starting point for rounds and scores
current_set = 0
player_1_scores = 0
player_2_scores = 0

# Loop until the specified number of rounds is reached
while current_set < number_of_rounds:
    print(f"The Current set is: {current_set + 1}")

# Get Player 1's choice and validate input
    player_1 = input(
        "Player One: Choose rock, paper, or scissors?").strip().lower()
    while player_1 not in answers:
        print(
            f"{player_1} is not a valid choice. Please choose rock, paper, or scissors.")
        player_1 = input(
            "Player One: Choose rock, paper, or scissors: ").strip().lower()

# Get Player 2's choice and validate input
    player_2 = input("Player Two: Choose rock, paper, or scissors: ").strip().lower(
    )
    while player_2 not in answers:

        print(
            f"{player_2} is not a valid choice. Please choose rock, paper, or scissors."
        )
        player_2 = input(
            "Player Two: Choose rock, paper, or scissors: ").strip().lower()


# Compare the players' choices and assign points

    if player_1 == player_2:
        print("It's a draw! Play the round again.")
         # 'continue' will restart the loop without advancing to the next round
        continue

    elif player_1 == "rock" and player_2 == "paper":
        print("Player Two wins this round!")
        player_2_scores += 1

    elif player_1 == "paper" and player_2 == "scissors":
        print("Player Two wins this round!")
        player_2_scores += 1

    elif player_1 == "scissors" and player_2 == "rock":
        print("Player Two wins this round!")
        player_2_scores += 1

    else:
        print("Player One wins this round")
        player_1_scores += 1

    # Only advance the round count if there's a winner
    current_set += 1

# Announce the winner
print(f"The scores are Player One: {
      player_1_scores} and Player Two: {player_2_scores}")

if player_1_scores > player_2_scores:
    print("Player One is the winner!")

else:
    print("Player Two is the winner!")
