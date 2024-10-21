import time

# define the keywords
def choices(choice):
    return choice in ["rock", "paper", "scissors"]

# define the rules
def determine_winner(player1, player2):
    if player1 == player2: # typing equal choice is a draw
        return "draw"
    # determine where Player1 is the winner
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock"):
        return "player1"
    # determine where Player2 is the winner
    else:
        return "player2"

# ask how many round wants be played
while True:
    try:
        rounds = int(input("Please enter rounds number you want to play: "))
        if rounds % 2 == 1:
            break
        else:
            print("Error: It is not possible to decide the winner, please type an en number!")
    except ValueError:
        print("Error: Enter a valid number!")

# starting numbers of rounds
player1_score = 0
player2_score = 0

# asking for count values, error messages, counting the rounds
for round_num in range(1, rounds + 1):
    print(f"\nRound {round_num}:")
    while True:
        player1_choice = input("Player 1, choose: rock, paper or scissors:").strip().lower()
        if choices(player1_choice):
            break
        else:
            print("Error: You must enter a valid answer (rock, paper, scissors)!")
    while True:
        player2_choice = input("Player 2, choose: rock, paper vagy scissors: ").strip().lower()
        if choices(player2_choice):
            break
        else:
            print("Error: You must enter a valid answer (rock, paper, scissors)!")
    
    #determine round winner
    winner = determine_winner(player1_choice, player2_choice)
    if winner == "player1":
        print(f"Player 1 won the round ({player1_choice} vs {player2_choice})!")
        player1_score += 1
    elif winner == "player2":
        print(f"Player 2 won the round ({player1_choice} vs {player2_choice})!")
        player2_score += 1
    else:
        print(f"Draw! ({player1_choice} vs {player2_choice})")

#determine final winner
time.sleep(1)
print("\nFinal result: ")
if player1_score > player2_score:
        print(f"Player 1 won with {player1_score} points, while Player 2 scored {player2_score} points.")
else:
    print(f"Player 2 won with {player2_score} points, while Player 1 scored {player1_score} points.")