# hogyan számoljuk a pontokat - fügvénnyel, mert mindig ez a rule:
def determine_winner(player1, player2, rounds, player_inputs):
    outcomes = {
        ("paper", "rock"): "Player1",
        ("scissor", "paper"): "Player1",
        ("rock", "scissor"): "Player1",
    }
    
    if (player1, player2) in outcomes:
        player_inputs["Score1"] += 1
        print(f"Player1 won Round_{rounds}!")
        return True #ezt majd később használom, hogy továbbléphet-e a ciklus vagy sem
    elif player1 == player2:
        print(f"Same choosen,let's repeat Round_{rounds}")
        return False #ezt majd később használom, hogy továbbléphet-e a ciklus vagy sem
    else: 
        player_inputs["Score2"] += 1 
        print(f"Player2 won Round_{rounds}!")
        return True #ezt majd később használom, hogy továbbléphet-e a ciklus vagy sem

valid_words = ["rock", "paper", "scissors"]
valid_words_str = "/".join(valid_words) #hogy rock/paper/scissor legyen a szövegben

players=[1,2] #játékosok száma - majd a for ciklushoz - bár ezt megmegadhattam volna a for i in players helyett "for i in range(1,3)"
player_inputs = {
    "Player1": "",
    "Score1" : 0,
    "Player2": "",
    "Score2" : 0,
}

#number of rounds:
while True:
    try:
        number_of_rounds = int(input("NUMBER of rounds you would like to play (odd): "))
        if number_of_rounds %2 ==0 or number_of_rounds <= 0:
            print(("Try again with an odd number!"))
        else:
            break
    except ValueError: #ezt a try - except-et találtam arra ha pl textet vinnének be szám heéyett és nem tudná átkonvertálni integerre
           continue
    
#players_answers:
rounds=1 #1-től indul a round
while rounds <= number_of_rounds:
    for i in players:
        player_input=input(f"Round_{rounds}: Choose {valid_words_str} Player{i}: ").strip().lower()

        while player_input not in valid_words:
            player_input=input(f"Round_{rounds}: It should be {valid_words_str} Player{i}: ").strip().lower()
        player_inputs[f"Player{i}"] = player_input

    if determine_winner(player_inputs["Player1"],player_inputs["Player2"],rounds,player_inputs):
        rounds +=1 #csak akkor lépünk tovább ha nem döntetlent játszottunk

#the winner is: sok sorban, hogy ne kelljen kétszer ugyanazt a stringet leírkálni printelésnél... 
if player_inputs["Score1"]>player_inputs["Score1"]: 
    winner = "Player1"
    winner_score=player_inputs["Score1"]
    looser_score=player_inputs["Score2"]
else:
    winner = "Player2"
    winner_score=player_inputs["Score2"]
    looser_score=player_inputs["Score1"]

print(f"Final winner is {winner} with {winner_score} point(s) against {looser_score} point(s).")
