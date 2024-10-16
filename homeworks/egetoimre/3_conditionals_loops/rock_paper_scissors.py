
while True:

    round = int(input("Hány kört szeretnétek játszani?"))

    if round % 2 == 0:
        print("A körök száma csak páratlan lehet!")
    else:
        break

rounds_played = 0
player_1_score = 0
player_2_score = 0

while rounds_played < round:

    while True:

        player_1 = input("Válasszon az első játékos lépést! (rock, paper, scissors)").lower().strip()

        if player_1 in ["rock", "paper", "scissors"]:
            break
        else:
            print("A választás csak 'rock', 'paper', 'scissors' lehet!")

    while True:

        player_2 = input("Válasszon a második játékos lépést! (rock, paper, scissors)").lower().strip()

        if player_2 in ["rock", "paper", "scissors"]:
            break
        else:
            print("A választás csak 'rock', 'paper', 'scissors' lehet!")

    if player_1 == player_2:
        print("Döntetlen! Ez a kör nem számít!")
    elif (player_1 == "paper" and player_2 == "rock") or (player_1 == "rock" and player_2 == "scissors") or (player_1 == "scissors" and player_2 == "paper"):
        print("A kört az első játékos nyerte!")
        rounds_played += 1
        player_1_score += 1
    elif (player_2 == "paper" and player_1 == "rock") or (player_2 == "rock" and player_1 == "scissors") or (player_2 == "scissors" and player_1 == "paper"):
        print("A kört a második játékos nyerte!")
        rounds_played += 1
        player_2_score += 1

print(f"A játéknak vége!{" Az első játékos gyözött " +str(player_1_score)+ " ponttal!" if player_1_score > player_2_score else " A második játékos gyözött " +str(player_2_score)+ " ponttal!"} ")



