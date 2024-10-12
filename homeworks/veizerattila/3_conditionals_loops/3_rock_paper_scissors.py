"""Feladat 2: while és for loop használata
- Hozz létre egy rock_paper_scissors.py nevű file-t, és kódold le a következő feladat megoldását:
- Írj egy python programot ami levezényli a kő-papír-olló játékot két játékos között.
    > A program kérje be, hogy hány kört akarnak játszani a játékosok.
    > Figyelj oda, hogy olyan számot kell megadnia a felhasználónak ami mellett nem tudnak döntetlent játszani! Ha nem ilyen számot ad meg, írj ki hibaüzenetet és addig kérd be újra a körök számát amíg páratlan számot nem ad meg
    > Ezután a program felváltva kérje be az első és második játékos válaszát, ami kizárólag a következő stringek valamelyik lehet: "rock", "paper", "scissors". Ellenkező esetben kezeld úgy a hibát ahogy a körök számánál.
    >Tárold a nyertesek pontjait, és minden kör végén növeld az aktuális játékos pontszámát.
    > A végén printeld ki ki nyert, és hány ponttal.
"""

# Változók deklarálása, ill. azon inpputok deklarálása, ami már a futás elején kelleni fog:
print("Let's play 'Rock-Paper-Scissors' with 2 players")
input("Press Enter if you're ready!")
actions = ['Rock', 'Paper', 'Scissors']
player1 = input("Name of Player1: ").strip().title()
player2 = input("Name of Player2: ").strip().title()
feedback = "Good" # köztes visszajelzés, az egyes input értékek sikeres elfogadásakor

# Először két külön változóban definiáltam a két játékos játékát, de itt elég összetett, így egy function-ba gyúrtam:
def valid_gamer_input(player, action):  # egyedi function definiálása, a későbbi játéklépések támogatására
    while True:
        action = input(f"{player}: What's your game? ").title()
        if action not in actions:
            print (f"{action} is an invalid input from {player}. Only {actions} are accepted. Try again. ")
        else:
            print(feedback)
            return action

# A külső while ciklus az újrajátszásra kérdez rá, a játék végén:
while True:
    points1 = 0
    points2 = 0
    # Belső while ciklus a körök bekérésére:
    while True: 
        rounds = int(input("How many rounds do you want to play? "))
        if rounds < 3 or rounds % 2 == 0 :
            print(f"{rounds} rounds won't declare a clear winner. Number of rounds must be odd. Please start over.")
        else:
            print(feedback)
            break    

    # Beágyazott while ciklus a játék futtatására:
    a = 0
    while a < (rounds):
        # itt hozom be a fent definiált function-t:
        action1 = valid_gamer_input(player1, actions)
        action2 = valid_gamer_input(player2, actions)

        rounds -= 1

        # játszma logikák definiálása és pontok számlálása
        if action1 == action2:
            print(f"Both {player1} and {player2} selected {action1}, it's a draw. No point gained.")
        elif (action1 == 'Rock' and action2 == 'Scissors') or (action1 == 'Scissors' and action2 == 'Paper') or (action1 == 'Paper'and action2 == 'Rock'):
            points1 += 1
            print(f"{action1} wins over {action2}. {player1} wins this round and has now {points1} point(s).")
        else:
            points2 += 1
            print(f"{action2} wins over {action1}. {player2} wins this round and has now {points2} point(s).")

        print(f"Remaining rounds: {rounds}")

    # A rounds körök végén (a 2. beágyazott while ciklus futás végén) a játék lezárása és eredmény kiírása:
    print("Game over.")
    if points1 > points2:
        print(f"{player1} wins over {player2} by {points1} vs {points2}")
    elif points1 == points2:
        print(f"Both {player1} and {player2} has the same points {points1} - {points2}")
    else:
        print(f"{player2} wins over {player1} by {points2} vs {points1}")

# A külső while ciklus végén rákérdezés, hogy akarunk-e újra játszani:
    start_over = input("Do you want to start over? (Y or N) ")
    if start_over.capitalize() != "Y":
        break