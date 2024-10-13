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
        print("döntetlen") #ezt nem számljuk meg
    else: # első szituáció 1. játékos nyeri a kört
        if gamer_1_choose == "rock" and gamer_2_choose == "scissors":
            gamer_1_score +=1
        else: # második szituáció 1. játékos nyeri a kört
            if gamer_1_choose == "paper" and gamer_2_choose == "rock":
                gamer_1_score +=1
            else: # harmadik szituáció 1. játékos nyeri a kört
                if gamer_1_choose == "scissors" and gamer_2_choose == "paper":
                    gamer_1_score +=1
                else: # az összes többi esetben 2. játékos nyeri a kört
                    gamer_2_score +=1 
        act_round +=1
        print(f"körök száma:{act_round}")

if gamer_1_score >= gamer_2_score:
    print("Győzőtt az 1. játékos")
else:
    print("Győzött a 2. játékos!")
