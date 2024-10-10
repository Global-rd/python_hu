from os import system

system("cls")


answer_selection = ["rock", "paper", "scissors"]


while True:
    rounds_to_play = int(input("Give an odd number for rounds: "))
    if rounds_to_play % 2 != 0:
        print(f"You will play {rounds_to_play} rounds.")
        break

round = 0

while True:
    player_1_answer = input("Choose rock, paper or scissor.")
    if player_1_answer in answer_selection:
        break

while True:
    player_2_answer = input("Choose rock, paper or scissor.")
    if player_2_answer in answer_selection:
        break
