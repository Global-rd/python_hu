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
p1_gave_up = False
p2_gave_up = False
input_message = "\n".join(f"{i+1}. {item}" for i,
                          item in enumerate(possible_choices))


i = 1
# for i in range(1, number_of_rounds + 1):
while i <= number_of_rounds:
    if someone_gave_up == True:
        print(f"A játék befejeződik mert valaki nem szeretne tovább játszani")
        break
    print(f"{i} kör kezdődik.\n")

    p1_answer = ""
    p1_answer_is_valid = False
    while someone_gave_up == False and p1_answer_is_valid == False:
        p1_answer = str(input(
            "Első játékos írd be a válaszod! Lehetséges válaszok: \n" + input_message + "\n"))
        if p1_answer in possible_choices:
            p1_answer_is_valid = True
            print(f"Helyes választás!\n")
            continue
        if p1_answer == 'X':
            p1_gave_up = True
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
            print(f"Helyes választás\n")
            continue
        if p2_answer == 'X':
            p2_gave_up = True
            someone_gave_up = True
            print(f"Második játékos feladta, a játék nem folytatódik\n")
            continue
        else:
            print(f"Helytelen válasz!")

    print(f"P1 válasza: {p1_answer} P2 válasza: {p2_answer} \n")
    if p1_gave_up == True or p2_gave_up == True:
        someone_gave_up == True

    if (p1_answer == p2_answer) and someone_gave_up == False:
        print(f"A két játékos válasza ugyanaz, szétlövés indul!!!\n")
        while p1_answer == p2_answer:
            p1_answer = ""
            p1_answer_is_valid = False
            while (someone_gave_up == False and p1_answer_is_valid == False):
                p1_answer = str(input(
                    "Első játékos írd be a válaszod! Lehetséges válaszok: \n" + input_message + "\n"))
                if p1_answer in possible_choices:
                    p1_answer_is_valid = True
                    print(f"Helyes választás!\n")
                    continue
                if p1_answer == 'X':
                    p1_gave_up = True
                    someone_gave_up = True
                    print(f"Első játékos feladta, a játék nem folytatódik!")
                    continue
                else:
                    p1_answer_is_valid = False
                    print(f"Helytelen valasz!")

            p2_answer = ""
            p2_answer_is_valid = False
            while someone_gave_up == False and p2_answer_is_valid == False:
                p2_answer = str(input(
                    "Második játékos írd be a válaszod! Lehetséges válaszok: \n" + input_message + "\n"))
                if p2_answer in possible_choices:
                    p2_answer_is_valid = True
                    print(f"Helyes választás\n")
                    continue
                if p2_answer == 'X':
                    p1_gave_up = True
                    someone_gave_up = True
                    print(f"Második játékos feladta, a játék nem folytatódik\n")
                    continue
                else:
                    print(f"Helytelen válasz!")

            print(f"P1 válasza: {p1_answer} P2 válasza: {p2_answer}")
            if p1_gave_up == True or p2_gave_up == True:
                someone_gave_up == True

            if someone_gave_up == True:
                log_message = ""
                if p1_gave_up == True and p2_gave_up == True:
                    log_message = f"Mindkét játékos feladat a játékot!"
                    print(log_message)
                elif (p1_gave_up == True and p2_gave_up == False):
                    log_message = f"P1 játékos feladata a játékot!"
                    print(log_message)
                elif (p2_gave_up == True and p1_gave_up == False):
                    log_message = f"P2 játékos feladata a játékot!"
                    print(log_message)
                break

            if (p1_answer == p2_answer):
                print(f"A szétlövéskor is ugyanaz a válasz, a szétlövés folytatódik!!!\n")

    if (someone_gave_up == True):
        print(f"Az {i} körben valaki feladata a játékot a játék nem folytatódik!\n")
        break
    else:
        if (p1_answer == "rock" and p2_answer == "scissors" or
                p1_answer == "paper" and p2_answer == "rock" or
                p1_answer == "scissors" and p2_answer == "paper"):
            print(f"P1 nyerte ezt a kört!\n")
            p1_points += 1
        else:
            print(f"P2 nyerte ezt a kört!\n")
            p2_points += 1

        print(
            f"Jelen állás szerint P1-nek {p1_points} pontja van P2-nek {p2_points} pontja van. \n")
        i += 1

if someone_gave_up == False:

    print(f"-----EREDMÉNYHÍRDETÉS -----")
    if (p1_points > p2_points):
        print(f"P1 játékos nyerte a játékot, {
            p1_points - p2_points}  pontal! ")
    else:
        print(f"P2 játékos nyerte a játékot, {
            p2_points - p1_points}  pontal! ")
