

def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return 0  # Döntetlen
    elif (player1_choice == "rock" and player2_choice == "scissors") or \
         (player1_choice == "scissors" and player2_choice == "paper") or \
         (player1_choice == "paper" and player2_choice == "rock"):
        return 1  # Első játékos nyer
    else:
        return 2  # Második játékos nyer

# Ellenőrizzük, hogy páratlan-e
def get_odd_rounds():
    while True:
        try:
            rounds = int(input("Hány kört akartok játszani? Páratlan, pozitív, egész számmal add meg!: "))
            if rounds > 0 and rounds % 2 == 1:
                return rounds
            else:
                print("Hiba: Pozitív, egész, páratlan számot adj meg!")
        except ValueError:
            print("Hiba: Kérlek adj meg egy pozitív, egész, páratlan számot! Nem olyan nehéz!")

# Ellenőrizzük a választ (csak "rock", "paper", "scissors")
def get_choice(player):
    while True:
        choice = input(f"{player}, válassz (rock, paper, scissors): ").strip().lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Hiba: Csak a 'rock', 'paper', 'scissors' válaszok megengedettek. Próbáld újra!")

# Játék indítása
def play_game():
    print("Üdvözöllek a kő-papír-olló játékban!")
    
    rounds = get_odd_rounds()  # Páratlan körszám bekérése
    player1_score = 0
    player2_score = 0
    completed_rounds = 0  # A ténylegesen lejátszott körök számának követése

    # Körök lejátszása addig, amíg valaki meg nem nyeri a játékot
    while completed_rounds < rounds:
        remaining_rounds = rounds - completed_rounds
        # Ha a pontkülönbség nagyobb, mint a hátralévő körök száma, vége a játéknak
        if abs(player1_score - player2_score) > remaining_rounds:
            print("\nA játék véget ért, mert már nem lehet fordítani!")
            break

        print(f"\n{completed_rounds + 1}. kör:")
        player1_choice = get_choice("Első játékos")
        player2_choice = get_choice("Második játékos")
        
        winner = determine_winner(player1_choice, player2_choice)
        
        if winner == 1:            
            player1_score += 1
            completed_rounds += 1
            print(f"Az első játékos nyerte a {completed_rounds}. kört! {player1_score} : {player2_score}")
        elif winner == 2:            
            player2_score += 1
            completed_rounds += 1
            print(f"A második játékos nyerte a {completed_rounds}. kört!  {player1_score} : {player2_score}")
        else:
            print("Döntetlen! Ez a kör nem számít bele a teljes körszámba.")
    
    # Végső eredmény
    print("\nJáték vége!")
    print(f"Első játékos pontszáma: {player1_score}")
    print(f"Második játékos pontszáma: {player2_score}")
    
    if player1_score > player2_score:
        print(f"Az első játékos nyert {player1_score-player2_score} ponttal!")
    else:
        print(f"A második játékos nyert {player2_score-player1_score} ponttal!")

# Program futtatása
if __name__ == "__main__":
    play_game()