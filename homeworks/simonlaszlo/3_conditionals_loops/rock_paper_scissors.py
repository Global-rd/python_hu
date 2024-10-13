input_word="A körök száma: "
while True:
   round=int(input(input_word))
   if round % 2 != 0:
      break
   else:
      input_word="Páratlan számot kérek: "
scor_1=0
scor_2=0
input_word2=("A következő kérdésekre csak 'rock', 'paper', 'scissors' a megfelelő válasz")
print(input_word2)

legal_answer=('rock', 'paper', 'scissors')
while round > 0:
     while True:
         player_1=input("Első játékos válastása: ")
         if player_1 in legal_answer:
            break
         else:
            print(input_word2)

     while True:
         player_2=input("Második játékos válastása: ")
         if player_2 in legal_answer:
             break
         else:
             print(input_word2)
    
     if player_1 != player_2:
         round -= 1
         if ((player_1 == 'rock') and (player_2 == 'scissors')) or ((player_1 == 'paper') and (player_2 == 'rock')) or ((player_1 == 'scissors') and (player_2 == 'paper')):
             scor_1 += 1
         else:
             scor_2 += 1
     else:
         print("Ez a kör döntetlen!")

print(f"Player 1: {scor_1}, Player 2: {scor_2}")
print(f"Az {'első' if scor_1 > scor_2 else 'második'} játékos győzött!")



         


      
