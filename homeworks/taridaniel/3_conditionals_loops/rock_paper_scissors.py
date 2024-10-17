while True:
    rounds = int(input("Enter the number of rounds (must be an odd number): "))
    if rounds % 2 != 0:
        break
    else:
        print("Error: Please enter an odd number.")

player1_points = 0
player2_points = 0
possible_choices = ["rock", "paper", "scissors"]

current_round = 1

# Play the game for a certain number of rounds
while current_round <= rounds:
#for word in range(rounds):
    while True:
        player1_choice = input("Player 1, enter your choice (rock, paper, or scissors): ")
        if player1_choice in possible_choices:
            break
        else:
            print("Error: Invalid choice. Please enter rock, paper, or scissors.")

    while True:
        player2_choice = input("Player 2, enter your choice (rock, paper, or scissors): ")
        if player2_choice in possible_choices:
            break
        else:
            print("Error: Invalid choice. Please enter rock, paper, or scissors.")

    if player1_choice == player2_choice:
        print("It's a tie, try this round again!")
        continue
    elif (player1_choice == "rock" and player2_choice == "scissors") or \
         (player1_choice == "scissors" and player2_choice == "paper") or \
         (player1_choice == "paper" and player2_choice == "rock"):
        player1_points += 1
    else:
        player2_points += 1
    
    current_round += 1

    print(f"Current score - Player 1: {player1_points}, Player 2: {player2_points}")

# Determine the winner
if player1_points > player2_points:
    print(f"Player 1 wins by {player1_points - player2_points} points!")
else:
    print(f"Player 2 wins by {player2_points - player1_points} points!")
