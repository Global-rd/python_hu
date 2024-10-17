"""
Author: Gaál István Tamás
Task: Homework-3 / 2
"""

first_player_score = 0
second_player_score = 0
number_of_rounds = 0
rounds = 0
list_of_opportunities = ["rock", "paper", "scissors"]

while number_of_rounds % 2 == 0:
    number_of_rounds = int(input("Please specify how many rounds you want to play, making sure it is an odd number:\n"))
    if number_of_rounds % 2 == 0:
        print("This number is even")
    else:
        break
    
while rounds < number_of_rounds:
    print(f"Turn {rounds+1}!")
    first_player_choose = input(f"First player please choose of them: {list_of_opportunities}!\n")
    while not first_player_choose in list_of_opportunities :
        first_player_choose = input(f"First player please choose of them: {list_of_opportunities}!\n")
    
    second_player_choose = input(f"Second player please choose of them: {list_of_opportunities}!\n")
    while not second_player_choose in list_of_opportunities :
        second_player_choose = input(f"Second player please choose of them: {list_of_opportunities}!\n")

    #DRAW
    if first_player_choose == second_player_choose:
        print("Draw")
        continue

    if first_player_choose == "rock":
        if second_player_choose == "paper":
            print("Second player win!\n")
            second_player_score += 1

        elif second_player_choose == "scissors":
            print("First player win!\n")
            first_player_score += 1

    if first_player_choose == "paper":
        if second_player_choose == "scissors":
            print("Second player win!\n")
            second_player_score += 1

        elif second_player_choose == "rock":
            print("First player win!\n")
            first_player_score += 1

    if first_player_choose == "scissors":
        if second_player_choose == "rock":
            print("Second player win!\n")
            second_player_score += 1

        elif second_player_choose == "paper":
            print("First player win!\n")
            first_player_score += 1

    rounds += 1

print(f"""First player score: {first_player_score}
Second player score: {second_player_score}
The winner is {"The First player!"if first_player_score > second_player_score else "The Second player!"}
""")