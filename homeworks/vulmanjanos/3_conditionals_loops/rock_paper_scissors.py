# körök defginiálása és a válasz
# páros körök elvetése 

accepted_round = 0
while accepted_round % 2 == 0:
    rounds = input("How many round do you want to play?: ")
    valid_rounds = True
    for char in rounds:
        if char not in "0123456789":
            valid_rounds = False
            break
    if valid_rounds and int(rounds) % 2 !=0:
        accepted_round = int(rounds)
    else:
        print("Please give me an odd number!")
  # induló pont meghatározása
  # elfogadható válaszodk definiálása listában
       
points = {"Player One": 0, "Player Two": 0}
accepted_options = ["rock", "paper", "scissors"]
# pluszban berakott sor a döntetlenek nem körként való számlálására, első lépés
current_round = 1
    # for loopal meg kell határozni, hogy meddig játszanak és a játokosok válaszait pedig while loop-pal, if-else
while current_round <= accepted_round:
# for i in range(accepted_round): cserélve egy while loopra
    player_1_accepted = False
    while not player_1_accepted:
        player_1_option = input("Player One, select an accepted option!: " )
        if player_1_option in accepted_options:
            player_1_accepted = True
        else:
            print("This is not an accepted option, please choose a right one: ")
    player_2_accepted = False
    while not player_2_accepted:
        player_2_option = input("Player Two, select an accepted option!: ")
        if player_2_option in accepted_options:
            player_2_accepted = True
        else:
            print("This is not an accepted option, please choose a right one: ")
    # az eredmények kalkulásása helyes válasz esetén +1-gyel
    if player_1_option == player_2_option:
        print("It's a draw")
        continue

    elif (player_1_option == "rock" and player_2_option == "scissors") or \
         (player_1_option == "paper" and player_2_option == "rock") or \
         (player_1_option == "scissors" and player_2_option == "paper"):
        points["Player One"] += 1
        print("Winner of the round : Player One")
    else:
        points["Player Two"] += 1
        print("Winner of the round : Player Two!")
    current_round +=1

 # végeredményhírdetés f-stringgel, a pontok / nevek beágyazásával, if-else
print(f"That's all folks! The final result: Player One: {points["Player One"]} score, Játékos 2: {points["Player Two"]} score")
if points["Player One"] > points["Player Two"]:
    print("And the winner is: Player One!!!")
else:
    print("And the winner is Player Two!!!")
