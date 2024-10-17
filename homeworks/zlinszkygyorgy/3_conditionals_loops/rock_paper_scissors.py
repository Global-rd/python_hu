# Input the number of rounds
while True:
        rounds = int(input("How many rounds do you want to play? "))
        if rounds % 2 == 0:
                print("Please enter an odd number to avoid ties.")
        else:
                break
    

player_1_score = 0
player_2_score = 0

for i in range(rounds):
    while True:
# Player 1 choice, ensures choice is valid
        while True:
            player_1_choice = input("Player 1, enter your choice (rock, paper, scissors): ").strip().lower()
            if player_1_choice in ["rock", "paper", "scissors"]:
                break
            else:
                print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

 # Player 2 choice, ensures choice is valid
        while True:
            player_2_choice = input("Player 2, enter your choice (rock, paper, scissors): ").strip().lower()
            if player_2_choice in ["rock", "paper", "scissors"]:
                break
            else:
                print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

# Defining the winner of the round
        if player_1_choice == player_2_choice:
            print("It's a tie! Please choose again.")
        elif (player_1_choice == "rock" and player_2_choice == "scissors") or \
             (player_1_choice == "scissors" and player_2_choice == "paper") or \
             (player_1_choice == "paper" and player_2_choice == "rock"):
            print("Player 1 won this round!")
            player_1_score += 1
            break
        else:
            print("Player 2 won this round!")
            player_2_score += 1
            break

# Print the final winner and the scores
print("Final Score:")
print(f"Player 1: {player_1_score}")
print(f"Player 2: {player_2_score}")

if player_1_score > player_2_score:
    print("Player 1 won the game!")
else:
    print("Player 2 won the game!")