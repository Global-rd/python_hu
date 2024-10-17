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

    # Első játékos választ
    while True:
      player_1_turn = input("Első játékos választ: ")
      if player_1_turn in options:
           break
    # Második játékos választ, de őt csak akkor engedi tovább ha mást választott mint az első játékos
    while True:
        player_2_turn = input("Második játékos választ: ")
        if player_2_turn in options and player_2_turn != player_1_turn:
            break  # Kilépünk, ha érvényes és eltérő választás történt
        print("A második játékos nem választhat ugyanazt! Próbáld újra.")

    # Játékszabály érvényesítése
    if (player_1_turn == "rock" and player_2_turn == "scissors") or (player_1_turn == "scissors" and player_2_turn == "paper") or (player_1_turn == "paper" and player_2_turn == "rock"):
        player1_score += 1
        print("Első játékos nyert ebben a körben!")
    else:
        player2_score += 1
        print("Második játékos nyert ebben a körben!")

# Végeredmény kiírása
print(f"Végeredmény: Első játékos {player1_score} pont, Második játékos {player2_score} pont")
if player1_score > player2_score:
    print("Első játékos nyert!")
else: print("Második játékos nyert!")
