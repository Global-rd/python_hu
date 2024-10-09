number_of_sets = int(input("Guys, how many sets do you want to play in a game? "))


if number_of_sets % 2 == 0:
    print(
        f"{number_of_sets} is even, therefore we can play draw. Please give me an odd number"
    )
else:
    print(f"The game will consist of {number_of_sets} sets")

player_1 = input("What's your choice mate? rock, paper, scissors?")
if player_1 == "rock" or player_1 == "paper" or player_1 == "scissors":
    print(f"Player One:{player_1}")
else:
    print(
        f"{player_1} is not a valid choice, please make your choice from rock, paper, scissors words"
    )

player_2 = input("What's your choice mate? rock, paper, scissors?")
if player_2 == "rock" or player_2 == "paper" or player_2 == "scissors":
    print(f"Player One:{player_2}")
else:
    print(
        f"{player_2} is not a valid choice, please make your choice from rock, paper, scissors words"
    )
