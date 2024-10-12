all_round = int(input("How many round do you wanna play?\n"))
player1_score = 0
player2_score = 0

while all_round % 2 ==0 :
    all_round = int(input("Wrong number, give me a new number\n"))


round = 1
while round <= all_round:
    print(f"Round: {round}")

    player1 = input("Player1 select Rock, Paper, or Scissor:\n")
    while player1 not in ["rock", "paper", "scissor"]:
        player1 = input("Please use lower case\n")


    player2 = input("Player2 select Rock, Paper, or Scissor:\n")
    while player2 not in ["rock", "paper", "scissor"]:
        player2 = input("Please use lower case\n")


    if player1 == "rock" and player2 == "paper":
        player2_score +=1
    elif player1 == "paper" and player2 == "scissor":
        player2_score +=1
    elif player1 == "scissor" and player2 == "rock":
        player2_score +=1
    elif player1 == player2:
        print("Tie")
    else:
        player1_score +=1
    
  
    round += 1


if player1_score < player2_score: 
    print(f"Player2 win with {player2_score} points.")
elif player2_score < player1_score:
    print(f"Player1 wint with {player1_score} points.")
else:
    print(f"Both player got {player1_score} points.") 