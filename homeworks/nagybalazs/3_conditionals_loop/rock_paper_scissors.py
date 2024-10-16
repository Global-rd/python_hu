"""
Írj egy python programot ami levezényli a kő-papír-olló játékot két játékos között. A program kérje be, hogy hány kört akarnak játszani a játékosok.
Figyelj oda, hogy olyan számot kell megadnia a felhasználónak ami mellett nem tudnak döntetlent játszani! Ha nem ilyen számot ad meg,
írj ki hibaüzenetet és addig kérd be újra a körök számát amíg páratlan számot nem ad meg. Ezután a program felváltva kérje be az első és második játékos válaszát,
ami kizárólag a következő stringek valamelyik lehet: "rock", "paper", "scissors". Ellenkező esetben kezeld úgy a hibát ahogy a körök számánál.
Tárold a nyertesek pontjait, és minden kör végén növeld az aktuális játékos pontszámát. A végén printeld ki ki nyert, és hány ponttal.
"""

print("Welcome to the big rock - paper - scissors game")
player_1 = input("Player 1 name: ").capitalize()
player_2 = input("Player 2 name: ").capitalize()


while True:
    game_round = int(input("How many rounds do you want to play? Please add odd number "))
    if game_round %2 != 0:
        break
    else:
        print ("Wrong number, try again.")


attempts = 0
p1_point = 0
p2_point = 0
while attempts < game_round:
    answer_player_1 = input(f"{player_1} enter your choice: /rock, paper or scissors/ ").lower().strip()
    answer_player_2 = input(f"{player_2} enter your choice: /rock, paper or scissors/ ").lower().strip()
    if answer_player_1 in ["rock", "paper", "scissors"] and answer_player_2 in ["rock", "paper", "scissors"]:
       attempts += 1
       if answer_player_1 == answer_player_2:
          attempts -= 1 
          print ("It's a tie, try again.")
       elif answer_player_1 == "rock" and answer_player_2 == "scissors":
            p1_point += 1
       elif answer_player_1 == "paper" and answer_player_2 == "rock":
            p1_point += 1
       elif answer_player_1 == "scissors" and answer_player_2 == "paper":
            p1_point += 1
       else:
            p2_point += 1
       continue      
    else:
        print("Please write rock, paper or scissors!")
else:
    if  p1_point > p2_point:
        winner_name = player_1
        winner_point = p1_point
    else:
        winner_name = player_2
        winner_point = p2_point
    print(f"The winner is {winner_name}! Winning games: {game_round}/{winner_point}")
