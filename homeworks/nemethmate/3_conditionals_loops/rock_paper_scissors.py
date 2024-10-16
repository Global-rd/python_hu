# Körök megadása
def get_odd_number():
    while True:
        try:
            rounds = int(input("Hány kört szeretnétek játszani? (páratlan szám): "))
            if rounds % 2 == 1:  # Ellenőrizzük, hogy páratlan szám-e
                return rounds
            else:
                print("Kérlek, adj meg egy páratlan számot!")  # Hibaüzenet páratlan szám hiányában
        except ValueError:
            print("Kérlek, egy érvényes számot adj meg!")  # Hibaüzenet érvénytelen bemenet esetén

# Játékosok választásai
def get_player_choice(player):
    while True:
        choice = input(f"{player}, kérlek válassz (rock, paper, scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice  # Visszatérünk a kiválasztott választással
        else:
            print("Kérlek, válassz a következőkből: rock, paper, scissors.")  # Hibaüzenet érvénytelen választás esetén

# Győztes kiválasztása
def determine_winner(choice1, choice2):
    if (choice1 == "rock" and choice2 == "scissors") or \
       (choice1 == "paper" and choice2 == "rock") or \
       (choice1 == "scissors" and choice2 == "paper"):
        return 1  # Első játékos nyer
    else:
        return 2  # Második játékos nyer

def main():
    print("Üdvözlünk a Kő-Papír-Olló játékban!")  # Üdvözlő üzenet
    
    rounds = get_odd_number()  # Kérjük be a körök számát
    player1_score = 0  # Első játékos pontszáma
    player2_score = 0  # Második játékos pontszáma

    # Körök lejátszása
    for round_number in range(1, rounds + 1):
        print(f"\n{round_number}. kör:")  # Kör száma
        while True:
            player1_choice = get_player_choice("1. Játékos")  # Első játékos választása
            player2_choice = get_player_choice("2. Játékos")  # Második játékos választása
            
            # Ellenőrizzük, hogy a választások eltérnek-e
            if player1_choice != player2_choice:
                break  # Ha eltérnek, kilépünk a ciklusból
            else:
                print("A választások nem eltérnek! Kérlek, válasszatok újra.")  # Hibaüzenet döntetlen esetén

        winner = determine_winner(player1_choice, player2_choice)  # Győztes meghatározása

        if winner == 1:
            player1_score += 1  # Első játékos pontjainak növelése
            print("1. Játékos nyert!")  # Győztes kiírása
        else:
            player2_score += 1  # Második játékos pontjainak növelése
            print("2. Játékos nyert!")  # Győztes kiírása

    # Játék vége
    print("\nA játék véget ért!")  # Játék vége üzenet
    print(f"1. Játékos pontjai: {player1_score}")  # Első játékos pontjainak kiírása
    print(f"2. Játékos pontjai: {player2_score}")  # Második játékos pontjainak kiírása

    # Győztes kiírása
    if player1_score > player2_score:
        print("1. Játékos nyert a játékot!")  # Ha az első játékos nyert
    else:
        print("2. Játékos nyert a játékot!")  # Ha a második játékos nyert

if __name__ == "__main__":
    main()  # A fő program indítása