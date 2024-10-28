print("---------------------Kő papír olló----------------------")

gamer_1_score = 0
gamer_2_score = 0
act_round = 0

while True: # ------------------------játék körök számának bekérése-------------------------
    game_round = int(input("Add meg a játék körök számát(csak páratlan szám megengedett): "))
    if game_round %2 != 0:
        break

while act_round < game_round:
    while True: # -----------------------------Válaszok bekérése----------------------------
        gamer_1_choose = input("Első játékos választása (csak a 'rock' 'paper' 'scissors' megengedett): ")
        if gamer_1_choose in ["rock", "paper", "scissors"]:
            break

    while True:
        gamer_2_choose = input("Második játékos választása (csak a 'rock' 'paper' 'scissors' megengedett): ")
        if gamer_2_choose in ["rock", "paper", "scissors"]:
            break
#-----------------------------Válaszok kiértékelése-----------------
    if gamer_1_choose == gamer_2_choose:
       print("döntetlen") #ezt nem számoljuk meg
    elif gamer_1_choose == "rock" and gamer_2_choose == "scissors": # első szituáció 1. játékos nyeri a kört
            gamer_1_score +=1
            act_round +=1
    elif gamer_1_choose == "paper" and gamer_2_choose == "rock": # második szituáció 1. játékos nyeri a kört
            gamer_1_score +=1
            act_round +=1
    elif gamer_1_choose == "scissors" and gamer_2_choose == "paper": # harmadik szituáció 1. játékos nyeri a kört
            gamer_1_score +=1
            act_round +=1
    else: # az összes többi esetben 2. játékos nyeri a kört
            gamer_2_score +=1
            act_round +=1
    print(f"körök száma:{act_round}")

#-----------------------------Eredmény kiírása------------------------
if gamer_1_score >= gamer_2_score:
    print(f"Győzőtt az 1. játékos, pontjainak száma:{gamer_1_score}.")
else:
    print(f"Győzött a 2. játékos, pontjainak száma:{gamer_2_score}.")
