def get_valid_rounds():
    while True:
        try:
            rounds = int(input("Hány kört szeretnétek játszani? "))
            if rounds <= 0:
                print("Hiba: A körök számának pozitívnak kell lennie.")
            elif rounds % 2 == 0:
                print(
                    "Hiba: Páratlan számú kört kell megadni a döntetlen elkerülése érdekében.")
            else:
                return rounds
        except ValueError:
            print("Hiba: Kérlek, adj meg egy érvényes számot.")


def get_valid_choice(player):
    valid_choices = ["rock", "paper", "scissors"]
    while True:
        choice = input(
            f"{player}. játékos választása (rock/paper/scissors): ").lower()
        if choice in valid_choices:
            return choice
        else:
            print(
                "Hiba: Érvénytelen választás. Kérlek, válassz a 'rock', 'paper' vagy 'scissors' közül.")


def play_round():
    while True:
        choice1 = get_valid_choice(1)
        choice2 = get_valid_choice(2)
        if choice1 == choice2:
            print("Döntetlen! Újrajátsszuk a kört.")
            continue
        if (choice1 == "rock" and choice2 == "scissors") or \
           (choice1 == "paper" and choice2 == "rock") or \
           (choice1 == "scissors" and choice2 == "paper"):
            return 1
        else:
            return 2


# Játék futtatása
rounds = get_valid_rounds()
player1_score = 0
player2_score = 0

for current_round in range(1, rounds + 1):
    print(f"\n{current_round}. kör:")
    winner = play_round()
    if winner == 1:
        player1_score += 1
        print("Az 1. játékos nyerte ezt a kört!")
    else:
        player2_score += 1
        print("A 2. játékos nyerte ezt a kört!")

print("\nJáték vége!")
print(f"1. játékos pontszáma: {player1_score}")
print(f"2. játékos pontszáma: {player2_score}")

if player1_score > player2_score:
    print("Az 1. játékos nyerte a játékot!")
else:
    print("A 2. játékos nyerte a játékot!")
