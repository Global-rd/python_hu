# Választási lehetőségek és a kezdő pontok
options = ["rock", "paper", "scissors"]
player1_score = 0
player2_score = 0

# Körök számának bekérése
while True:
    chosen_rounds = int(input("Hány kört szeretnél játszani? "))
    if chosen_rounds % 2 != 0:
        print("---- Kezdődhet a játék. -----")
        break
    else:
        print("Páratlan körrel indul csak a játék.")

# A kiválasztott számnak megfelelő körök lejátszása:
for rounds in range(chosen_rounds):

    # Mindkét játékos választ
    while True:
      player_1_turn = input("Első játékos választ: ")
      if player_1_turn in options:
           break

    while True:
      player_2_turn = input("Második játékos választ: ")
      if player_2_turn in options:
           break
    
    # Játékszabály érvényesítése
    if player_1_turn == player_2_turn:
        print("Döntetlen!")
    elif (player_1_turn == "rock" and player_2_turn == "scissors") or (player_1_turn == "scissors" and player_2_turn == "paper") or (player_1_turn == "paper" and player_2_turn == "rock"):
        player1_score += 1
        print("Első játékos nyert ebben a körben!")
    else:
        player2_score += 1
        print("Második játékos nyert ebben a körben!")

# Végeredmény kiírása
print(f"Végeredmény: Első játékos {player1_score} pont, Második játékos {player2_score} pont")
if player1_score > player2_score:
    print("Első játékos nyert!")
elif player2_score > player1_score:
    print("Második játékos nyert!")
else: print("Döntetlen a játék!")
