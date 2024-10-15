while True:
    all_round = int(input("How many rounds do you want to play? "))
    if all_round % 2 != 0:
        break
    print("The number of rounds must be odd. Try again.")

player1_score = 0
player2_score = 0

round = 1
while round <= all_round:
    print(f"Round: {round}")

    player_1_choice  = input("Player1 choice Rock, Paper, or Scissor:\n")
    while player_1_choice not in ["rock", "paper", "scissor"]:
        player_1_choice = input("Wrong input, please provide either rock, paper or scissor.\n")

    player_2_choice = input("Player2 choice Rock, Paper, or Scissor:\n")
    while player_2_choice not in ["rock", "paper", "scissor"]:
        player_2_choice = input("Wrong input, please provide either rock, paper, or scissor.\n")

    if player_1_choice == player_2_choice:
        print("Tie")
        continue
    if player_1_choice == "rock" and player_2_choice == "paper":
        player2_score +=1
    elif player_1_choice == "paper" and player_2_choice == "scissor":
        player2_score +=1
    elif player_1_choice == "scissor" and player_2_choice == "rock":
        player2_score +=1
    else:
        player1_score +=1
      
    round += 1

if player1_score < player2_score: 
    print(f"Player2 win with {player2_score} points.")
elif player2_score < player1_score:
    print(f"Player1 wint with {player1_score} points.")
else:
    print(f"Both player got {player1_score} points.") 