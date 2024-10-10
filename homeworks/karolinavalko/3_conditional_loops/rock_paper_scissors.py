from os import system

system("cls")


answer_selection = ["rock", "paper", "scissors"]
player_1_score = 0
player_2_score = 0
player_1_wins = ["rock_scissors", "paper_rock", "scissors_paper"]
player_2_wins = ["rock_paper", "paper_scissors", "scissors_rock"]
round = 0


while True:
    rounds_to_play = int(input("Give an odd number for rounds: "))
    if rounds_to_play % 2 != 0:
        print(f"You will play {rounds_to_play} rounds.")
        break

while rounds_to_play > round:
    print(f"Round nr. {round+1}")
    while True:
        player_1_answer = input("Player 1 choose rock, paper or scissors.")
        if player_1_answer in answer_selection:
            break

    while True:
        player_2_answer = input("Player 2 choose rock, paper or scissors.")
        if player_2_answer in answer_selection:
            break

    game_outcome = player_1_answer + "_" + player_2_answer

    if game_outcome in player_1_wins:
        print("Player 1 wins")
        player_1_score += 1
        round += 1
    elif game_outcome in player_2_wins:
        print("Player 2 wins")
        player_2_score += 1
        round += 1
    else:
        print(f"Tie. Rematch.")

print(
    f"The winner is Player 1 with {player_1_score} points."
    if player_1_score > player_2_score
    else f"The winner is Player 2 with {player_2_score} points."
)
