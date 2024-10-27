game_round = int(input("Hány fordulóig megyünk ? :"))
while game_round % 2 != 0 :
    break
else: 
    print("Ha páros akkor lehet döntetlen is .")
    game_round = int(input("Hány fordulóig megyünk ? :"))
print(f"{game_round} kör lesz a játék hossza")


counter = 0
count1 = 0
count2 = 0
while counter < game_round :
    while True:
        gamer1 = str(input("kérem az első játékost : ( K P O betűket) : ").upper().strip())
        if gamer1 == "K" or gamer1 == "P" or gamer1 == "O":
            print("Megfelelő")
            break
        else:
            print("Nem megfelelő")
            gamer1 = str(input("kérem az első játékost ( K P O betűket) : ").upper().strip())
    while True:
        gamer2 = str(input("kérem az második játékost : ( K P O betűket): ").upper().strip())
        if gamer2 == "K" or gamer2 == "P" or gamer2 == "O":
            print("Megfelelő")
            break
        else:
            print("Nem megfelelő")
        gamer2 = str(input("kérem az második játékost : ( K P O betűket) : ").upper().strip())  
        
    if gamer1 == gamer2 :
        print("Ez a kör nem játszik !")
    elif (gamer1=="P" and gamer2=="K") or (gamer1=="K" and gamer2=="O") or (gamer1=="O" and gamer2=="P"):   
        print("A kört az 1. játékoe nyerte. ")
        counter += 1
        count1 += 1
    elif (gamer2=="P" and gamer1=="K") or (gamer2=="K" and gamer1=="O") or (gamer2=="O" and gamer1=="P"):
        print("A kört az 2. játékoe nyerte. ")   
        counter += 1
        count2 += 1
        
print(f"Első játékos pontja    : {count1}")
print(f"Második játékos pontja : {count2}")
