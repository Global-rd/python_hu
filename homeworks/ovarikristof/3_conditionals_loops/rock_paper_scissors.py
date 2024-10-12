 BEKÉRÜNK NEVEKET A FELHASZNÁLÓKHOZ:
player_1 = input("Please enter a name for Player 1: ")
player_2 = input("Please enter a name for Player 2: ")

# BEKÉRJÜK, HOGY HÁNY KÖRT AKARNAK JÁTSZANI,
#ÉS MEGHATÁROZZUK, HOGY CSAK PÁRATLAN KÖRÖK MEGADÁSA UTÁN INDUL A JÁTÉK
def game_rounds():
    while True:
        try:
            rounds_want_to_play = int(input("Please enter how many rounds do you want to play: "))
            if rounds_want_to_play % 2 == 1:
                return rounds_want_to_play
            else:
                print("Please enter an odd number, else there won't be a winner!")
        except ValueError:
            print("Please enter a valid number!")


#MEGKÉRJÜK A JÁTÉKOSOKAT, HOGY ADJÁK MEG A VÁLASZAIKAT
def get_players_1_choice(player_1):
    while True:
        player_1_choice = input(f"{player_1}, please enter your choice (rock, paper, scissors): ").lower()
        if player_1_choice in ["rock", "paper", "scissors"]:
            return player_1_choice
        else:
            print("Please enter only the following: rock, paper, scissors!")

def get_players_2_choice(player_2):    
    while True:
        player_2_choice = input(f"{player_2}, please enter your choice (rock, paper, scissors): ").lower()
        if player_2_choice in ["rock", "paper", "scissors"]:
            return player_2_choice
        else:
            print("Please enter only the following: rock, paper, scissors!")

#MEGHATÁROZZUK, HOGY A JÁTÉKOSOK VÁLASZAI ALAPJÁN MELYIKÜK AZ AMELYIK PONTOT SZEREZ A VÁLASZTÁSA ALAPJÁN
def determine_winner(choice_1, choice_2):
    if choice_1 == choice_2:
        return 0                                                 #DÖNTETLEN
    elif (choice_1 == "rock" and choice_2 == "scissors") or \
         (choice_1 == "scissors" and choice_2 == "paper") or \
         (choice_1 == "paper" and choice_2 == "rock"):
        return 1                                                 #PLAYER_1 NYERT
    else:
        return 2                                                 #PLAYER_2 NYERT

#A JÁTÉK DEFINIÁLÁSA:
def rock_paper_scissors():
    rounds_want_to_play = game_rounds()
    player_1_score = 0
    player_2_score = 0

    for i in range(rounds_want_to_play):
        print(f"----- {i+1}. kör -----")                        #VISSZAADJA, HOGY MELYIK KÖR KÖVETKEZIK
        player_1_choice = get_players_1_choice(player_1)        
        player_2_choice = get_players_2_choice(player_2)


#KIÍRJUK, HOGY MELYIK JÁTÉKOS NYERTE A KÖRT
        winner = determine_winner(player_1_choice, player_2_choice)

        if winner == 1:
            print(f"{player_1} won this round!")
            player_1_score += 1
        elif winner == 2:
            print(f"{player_2} won this round!")
            player_2_score += 1
        else:
            print("This round is a tie!")

#KIÍRJA, HOGY MELYIK JÁTÉKOSNAK HÁNY PONTJA LETT A JÁTÉK SORÁN
    print(f"\nRESULT:")
    print(f"{player_1}: {player_1_score} pont")
    print(f"{player_2}: {player_2_score} pont")

#A PONTSZÁMOK ALAPJÁN KIADJA A PROGRAM, HOGY KI NYERTE A JÁTÉKOT
    if player_1_score > player_2_score:
        print(f"{player_1} won the game!!!")
    elif player_2_score > player_1_score:
        print(f"{player_2} won the game!!!")
    else:
        print("This game is a tie!!!")

#JÁTÉK FUTTATÁSA
rock_paper_scissors()
