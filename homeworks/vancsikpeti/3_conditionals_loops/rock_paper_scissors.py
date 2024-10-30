
def answer(symbol=""):
    right_symbols = ["rock", "paper", "scissors"]
    while symbol not in right_symbols:
        symbol = input("Please, enter the symbol: ")
        if symbol not in right_symbols:
            print("The symbol is incorrect. Please choose from the following: rock, paper, scissors")
    return symbol   

def whowins(answer1, answer2):
    winner = ""
    if answer1 == answer2: winner = "both"
    if answer1 == "paper" and answer2 == "rock": winner = answer1
    if answer1 == "paper" and answer2 == "scissors": winner = answer2
    if answer1 == "rock" and answer2 == "paper": winner = answer2
    if answer1 == "rock" and answer2 == "scissors": winner = answer1
    if answer1 == "scissors" and answer2 == "paper": winner = answer1
    if answer1 == "scissors" and answer2 == "rock": winner = answer2
    return winner

number_of_rounds = 2
right_symbols = ["rock", "paper", "scissors"]

while number_of_rounds % 2 == 0 or number_of_rounds < 0:
    number_of_rounds = int(input("How many rounds do you want to play?" ))
    if number_of_rounds % 2 == 0 or number_of_rounds < 0:
        print("The number of rounds cannot be even.")

round = 1
player1_answer = ""
player1_points = 0
player2_answer = ""
player2_points = 0
winner = ""
diff_point = 0

while round < number_of_rounds+1:
    print(f"{round}. round")
    print("First player!")
    player1_answer = answer()
    print("Second player!")
    player2_answer = answer()
    winner = whowins(player1_answer, player2_answer)
    if winner == "both":
        print("Same symbol. Restarted the round.")
        continue
    elif winner == player1_answer:
        player1_points += 1
    elif winner == player2_answer:
        player2_points += 1
    # print(f"The winner of the round is the {whowins(player1_answer, player2_answer)}. The score of the game: Player1-Player2: {player1_points}-{player2_points}")
    round += 1    

if player1_points > player2_points: 
    winner = "Player 1"
    diff_point = player1_points-player2_points
elif player1_points < player2_points:
    winner = "Player 2"
    diff_point = player2_points-player1_points
elif player1_points is player2_points:
    winner = "both of them"
    diff_point = 0
else:
    "ERROR"

print(f"The winner is the {winner} with {diff_point} point(s).")

"""
Feladat 2.
Írj egy python programot ami levezényli a kő-papír-olló játékot két játékos között. 
A program kérje be, hogy hány kört akarnak játszani a játékosok. 
Figyelj oda, hogy olyan számot kell megadnia a felhasználónak ami mellett nem tudnak döntetlent játszani! 
Ha nem ilyen számot ad meg, írj ki hibaüzenetet és addig kérd be újra a körök számát amíg páratlan számot nem ad meg. 
Ezután a program felváltva kérje be az első és második játékos válaszát, ami kizárólag a következő stringek valamelyik lehet: "rock", "paper", "scissors". 
Ellenkező esetben kezeld úgy a hibát ahogy a körök számánál. 
Tárold a nyertesek pontjait, és minden kör végén növeld az aktuális játékos pontszámát. 
A végén printeld ki ki nyert, és hány ponttal.
"""

