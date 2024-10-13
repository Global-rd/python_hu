"""
rock_paper_scissors.py --- Asztalos Lajos --- 2024.10.13
"""
#parameters
RPS = list(["kő","papír", "olló"])
a_score = 0
b_score = 0

#input rounds
i=0
while i == 0:
    rounds_num=int(input("Add meg a fordulók számát:"))
    i=rounds_num % 2
    if i==0: print("Csak páratlan számot adhatsz meg!")
print(f"Kezdhetjük a játékot {rounds_num} fordulóval.")


#play
round = 0
while round < rounds_num:
    round += 1
    print(f"Forduló:{round}, A:{a_score}, B:{b_score}")
    #input first bet
    i=False
    while i==False:
        a_player_bet = input(f"Az első játékos {round}. tétje:")
        for bet in RPS:
            i = (a_player_bet==bet) or i
        if i==False: 
            print("A megadott érték csak kő, papír vagy olló lehet!")
    #input second bet
    i=False
    while i==False:
        b_player_bet = input(f"A második játékos {round}. tétje:")
        for bet in RPS:
            i = (b_player_bet==bet) or i
        if i==False: 
            print("A megadott érték csak kő, papír vagy olló lehet!")
    #evaluation
    if a_player_bet == "kő":
        if b_player_bet == "papír":
            b_score += 1
            print("A második játékos nyerte a fordulót, mert a papír becsomagolja a kővet.")
        elif b_player_bet == "olló":
            a_score += 1
            print("Az első játékos nyerte a fordulót, mert a kő összetöri az ollót.")
        else: 
            round += -1
            print("Az azonos tétek miatt újra kell játszani a fordulót!")
    elif a_player_bet == "papír":
        if b_player_bet == "olló":
            b_score += 1
            print("A második játékos nyerte a fordulót, mert az olló elvágja a papírt.")     
        elif b_player_bet == "kő":
            a_score += 1
            print("Az első játékos nyerte a fordulót, mert a papír becsomagolja a kővet.")
        else: 
            round += -1
            print("Az azonos tétek miatt újra kell játszani a fordulót!")
    elif a_player_bet == "olló": 
        if b_player_bet == "kő":
            b_score += 1
            print("A második játékos nyerte a fordulót, mert a kő összetőri az ollót.")
        elif b_player_bet == "papír":
            a_score += 1
            print("Az első játékos nyerte a fordulót, mert az olló elvágja a papírt.")
        else:
            round += -1
            print("Az azonos tétek miatt újra kell játszani a fordulót")
    print()
#result
if a_score > b_score:
    print(f"Az első játékos nyert {a_score}:{b_score} arányban")
else: print(f"A második játékos nyert {b_score}:{a_score} arányban") 