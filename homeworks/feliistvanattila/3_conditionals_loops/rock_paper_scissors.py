print(f"A program be fogja kérni hogy hány kört szeretnétek játszani \n")
print(f"Kérlek páratlan számot adj meg! Jó játékot :D:D:D!!! ")
possible_choices = ["rock", "paper", "scissors"]


can_the_game_started = False
number_of_rounds = 0
while can_the_game_started == False:
    number_of_rounds = int(input(f"Hány kört szeretnétek játszani?: "))
    if ((number_of_rounds % 2) != 0):
        print(f"Jó szamot adtál meg, jó játékot!!! :)")
        can_the_game_started = True
    else:
        print(f"Kérlek páratlan számot adj meg!!!")
        can_the_game_started = False

# Init game variables
p1_points = 0
p2_points = 0
someone_gave_up = False
someone_gave_up_character = "X"
input_message = "\n".join(f"{i+1}. {item}" for i,
                          item in enumerate(possible_choices))

for i in range(1, number_of_rounds + 1):
    if someone_gave_up == True:
        print(f"A játék befejeződik mert valaki nem szeretne tovább játszani")
        break
    print(f"{i} kör kezdődik.")

    p1_answer = ""
    p1_answer_is_valid = False
    while someone_gave_up == False and p1_answer_is_valid == False:
        p1_answer = str(input(
            "Első játékos írd be a válaszod! Lehetséges válaszok: \n" + input_message + "\n"))
        if p1_answer in possible_choices:
            p1_answer_is_valid = True
            print(f"Helyes választás!")
            continue
        if p1_answer == 'X':
            someone_gave_up = True
            print(f"Első játékos feladta, a játék nem folytatódik!")
            continue
        else:
            print(f"Helytelen valasz!")

    p2_answer = ""
    p2_answer_is_valid = False
    while someone_gave_up == False and p2_answer_is_valid == False:
        p2_answer = str(input(
            "Második játékos írd be a válaszod! Lehetséges válaszok: \n" + input_message + "\n"))
        if p2_answer in possible_choices:
            p2_answer_is_valid = True
            print(f"Helyes választás")
            continue
        if p2_answer == 'X':
            someone_gave_up = True
            print(f"Második játékos feladta, a játék nem folytatódik")
            continue
        else:
            print(f"Helytelen válasz!")

    print(f"P1 válasza: {p1_answer} P2 válasza: {p2_answer}")
    if p1_answer == p2_answer:
        print(f"Döntetlen! Senki sem kap pontot")
    
    elif (p1_answer == "rock" and p2_answer == "scissors" or \
            p1_answer == "paper" and p2_answer == "rock" or \
            p1_answer == "scissors" and p2_answer == "paper"):
        print(f"P1 nyerte ezt a kört!")
        p1_points += 1
    else:
        print(f"P2 nyerte ezt a kört!")
        p2_points += 1


    print(
        f"Jelen állás szerint P1-nek {p1_points} pontja van P2-nek {p2_points} pontja van. ")
    
if p1_points == p2_points:
    print(f"A jéték döntetlenre végződött :)!! {p1_points} - {p2_points} eredményel") 
elif p1_points > p2_points:
    print(f"P1 játékos nyerte a játékot, {p1_points - p2_points}  pontal! ")
else:
    print(f"P2 játékos nyerte a játékot, {p2_points - p1_points}  pontal! ")

