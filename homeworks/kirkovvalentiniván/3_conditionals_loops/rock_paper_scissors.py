print("Welcome to the game. You will play rock-paper-scissors!")
player_1_name = str(input("Player 1 please enter your name here: ")).title().strip()
player_2_name = str(input("Player 2 please enter your name here: ")).title().strip()

#Declaring the number of rounds
while True:
    rounds = int(input("How many rounds would you like to play? Please write your answer using only whole numbers:  "))
    if rounds % 2 != 0:
        break
    print("Incorrect number. The outcome could be draw. To avoid this please write down an odd number.")

#Necessary starting variables for the project
correct_words = ["rock","paper","scissors"]
player_1_score = 0
player_2_score = 0

#The game
while rounds > 0:
    while True:
        player_1_word = str(input("Pick rock, paper or scissors and write your answer here: ")).lower().strip()
        if player_1_word in correct_words:
            break
        print("Incorrect word, please choose a correct one.")
    
    while True:         
        player_2_word = str(input("Pick rock, paper or scissors and write your answer here: ")).lower().strip()
        if player_2_word in correct_words:
            break
        print("Incorrect word, please choose a correct one")

    if player_1_word != player_2_word:
        rounds -= 1
        if  (player_1_word == "rock" and player_2_word == "scissors") or \
            (player_1_word == "paper" and player_2_word == "rock") or \
            (player_1_word == "scissors" and player_2_word == "paper"):
            print(f"The winner of the round is {player_1_name}.")
            player_1_score =+ 1
        else:
            print(f"The winner of the round is {player_2_name}.")
            player_2_score += 1
    else:
        print("This round is even, please play again.")

#Results
if player_1_score > player_2_score:
    print(f"The winner is {player_1_name}. {player_1_name} won by {player_1_score} points ahead of {player_2_name} who has {player_2_score} points.")
print(f"The winner is {player_2_name}. {player_2_name} won by {player_2_score} points ahead of {player_1_name} who has {player_1_score} points.")
