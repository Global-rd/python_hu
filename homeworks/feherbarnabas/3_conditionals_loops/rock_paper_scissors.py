while True:
    rounds = int(input("Enter the number of rounds: "))

    if rounds % 2 == 1:
        break

    else:
        print("ERROR: Must be an odd number!")

player1_score = 0
player2_score = 0
current_round = 1

#Player 1 
while current_round <= rounds:
    print(f"Round {current_round}:")

    while True:
        player_1 = input("Player 1: rock, paper or scissors?").strip().lower()
        if player_1 in ["rock", "paper", "scissors"]:
            break
        else: 
            print("ERROR: rock, paper, scissors are the possibilities.")

#Player 2
    while True:
        player_2 = input("Player 2: rock, paper or scissors?").strip().lower()
        if player_2 in ["rock", "paper", "scissors"]:
            break
        else: 
            print("ERROR: rock, paper, scissors are the possibilities.")

    if player_1 == player_2:
            print("It's a tie!")
            continue
    elif(player_1 == "rock" and player_2 == "scissors") or (player_1 == "paper" and player_2 == "rock") or(player_1 == "scissors" and player_2 == "paper"):
            print("Player 1 wins this round!")
            player1_score += 1
    else:
            print("Player 2 wins this round!")
            player2_score += 1
    current_round += 1

print("Final scores:")
print(f"Player 1: {player1_score}")
print(f"Player 2: {player2_score}")

if player1_score > player2_score:
    print(f"Player 1 wins the game with {player1_score} points!")
elif player2_score > player1_score:
    print(f"Player 2 wins the game with {player2_score} points!")
else:
    print("The game ends in a tie!")