
# Adjuk meg hány kört akarunk játszani, figyeljünk oda a végeredmény nem lehet döntetlen
while True:
    try:
        count_rounds = int(input("How many turns would you like to play? Write an odd number: "))
        if count_rounds % 2 == 0:
            print(f"Must be a winner at the end! Give an odd number:")
        else:
            break
    except ValueError:
        print("Have to write correct number!")


# Pontszámok
player1_score = 0
player2_score = 0

#Körök iterálása
for round in range(count_rounds):
    print(f"\n{round + 1}. kör: ")

    #Első játékos köre:
    while True:
        player1_choice = input("Player 1 turn: 'rock', 'paper' or 'scissors'?: " ).lower()
        if player1_choice in ["rock", "paper", "scissors"]:
            break
        else:
            print(f"Choose one of them: 'rock', 'paper', 'scissors': ")

    #Második játékos köre:
    while True:
        player2_choice = input("Player 2 turn: 'rock', 'paper' or 'scissors'?: " ).lower()
        if player2_choice in ["rock", "paper", "scissors"]:
            break
        else:
            print("Choose one of them: 'rock', 'paper', 'scissors': ")

    #Eredmény meghatározása:
    if player1_choice == player2_choice:
        print("The result is a draw")
    elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
         (player1_choice == 'scissors' and player2_choice == 'paper') or \
         (player1_choice == 'paper' and player2_choice == 'rock'):
        print("Player 1 won that round")
        player1_score += 1
    else:
        print("Player 2 won that round")
        player2_score += 1

#Játék véget ért, eredmények kiírása
print("\nGame Over")
print(f"Player 1 score: {player1_score}")
print(f"Player 2 score: {player2_score}")

if player1_score > player2_score:
    print("The winner is Player 1")
elif player1_score < player2_score:
    print("The winner is Player 2")
else:
    print("The result is draw")