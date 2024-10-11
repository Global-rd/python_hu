# homework - Nagy Norbert

# define numbers of rounds
while True:
    rounds = int(input("Please define how many rounds would you like to play: "))
    if rounds < 3 or rounds%2 == 0:
        print("Invalid input, please define a positive odd number which grater than 2")
    else:
        print("Thanks, valid input.")
        break

valid_signs = ["rock","paper","scissors"]

# define and validate signs in one round
def add_input_sign(player):
    print(f" -  {player}.player  - ")
    while True:
        sign = input("Please add your sign: ")
        input_sign = sign.strip().lower()
        if sign not in valid_signs:
            print("Invalid input: {sign}, try again")
        else:
            print(f"Thanks, valid input: {sign}.")
            break

    return input_sign

# evaluate signs and summerize points in one round
def evaluate_signs(sum_points_1,sum_points_2,player_1_sign,player_2_sign):
    if player_1_sign == "rock" and player_2_sign == "paper":
        sum_points_2 += 1
    elif player_1_sign == "rock" and player_2_sign == "scissors":
        sum_points_1 += 1
    elif player_1_sign == "paper" and player_2_sign == "rock":
        sum_points_1 += 1
    elif player_1_sign == "paper" and player_2_sign == "scissors":
        sum_points_2 += 1
    elif player_1_sign == "scissors" and player_2_sign == "rock":
        sum_points_2 += 1
    elif player_1_sign == "scissors" and player_2_sign == "paper":
        sum_points_1 += 1
    return sum_points_1,sum_points_2

sum_point_1_player = 0
sum_point_2_player = 0

input_list_1 = []
input_list_2 = []

# iterate on all round and updates points
for id, i in enumerate(range(rounds),1):
    print(f" ----- {id}. round ----- ")
    player_1_sign = add_input_sign(1)
    input_list_1.append(player_1_sign)
    player_2_sign = add_input_sign(2)
    input_list_2.append(player_2_sign)
    
    sum_point_1_player,sum_point_2_player = evaluate_signs(sum_point_1_player,sum_point_2_player,player_1_sign,player_2_sign)

print(f"1st player signs: {input_list_1}")
print(f"2nd player signs: {input_list_2}")

# decide who is the winner
winner = sum_point_1_player - sum_point_2_player
if winner > 0:
    print(f"Winner is 1st player with {sum_point_1_player} points.")
elif winner < 0:
    print(f"Winner is 2nd player with {sum_point_2_player} points.")
else:
    print("Same points, no winner.")