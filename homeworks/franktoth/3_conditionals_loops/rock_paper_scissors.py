# Get player names and desired number of rounds
player1_name = input("Player 1, please enter your name: ")
player2_name = input("Player 2, please enter your name: ")

while True:
  try:
    rounds = int(input("How many rounds would you like to play? (Must be an odd number): "))
    if rounds % 2 == 0:
      print("The number of rounds must be odd. Please try again.")
    else:
      break
  except ValueError:
    print("Please enter a valid number of rounds.")

# Initialize player scores
player1_score = 0
player2_score = 0

# Function to get player's choice
def get_choice(player_name):
    while True:
        choice = input(f"{player_name}, please choose rock, paper, or scissors: ").lower()
        if choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
        else:
            return choice

# Play the game
for round_num in range(1, rounds + 1):
    print(f"\nRound {round_num}")

    while True:
        player1_choice = get_choice(player1_name)
        player2_choice = get_choice(player2_name)

        if player1_choice == player2_choice:
            print("It's a tie! Both players chose the same sign. Please choose again.")
        else:
            if (player1_choice == "rock" and player2_choice == "scissors") or \
              (player1_choice == "paper" and player2_choice == "rock") or \
              (player1_choice == "scissors" and player2_choice == "paper"):
                print(f"{player1_name} wins this round!")
                player1_score += 1
            else:
                print(f"{player2_name} wins this round!")
                player2_score += 1
            break

# Determine the overall winner
if player1_score > player2_score:
    print(f"\n{player1_name} wins the game with a score of {player1_score} to {player2_score}!")
else:
    print(f"\n{player2_name} wins the game with a score of {player2_score} to {player1_score}!")