'''
3. házi feladat

Feladat 2: Rock Paper Scissors
(while és for loop használata)
'''

import random

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../_0_helpers')))

from terminal_clearer import clear_terminal

clear_terminal()

while True:
    # Ask the user for input
    turns_nr = int(input("How many rounds would you like to play in Rock Paper Scissors? (Enter an odd number): ").strip())

    # Check if the number is odd
    if turns_nr % 2 != 0:
        break
    else:
        print("That's an even number, try again.")

# Tuple to store the options
rock_paper_scissors_options = ("Rock", "Paper", "Scissors")

player_score = 0
computer_score = 0
tie = 0

current_turn = 1

while current_turn <= turns_nr:
    clear_terminal()
    print(f"Turn {current_turn}.")

    # Computer makes a random choice
    computer_choice = random.choice(rock_paper_scissors_options)

    # Ask the user for their choice
    while True:
        # Ask the user for input
        print(f"Choose your option: \n1: Rock \n2: Paper\n3: Scissors")
        user_input = int(input("Enter 1, 2, or 3: "))
        # Check if the user_input is 1,2 or 3
        if user_input == 1 or user_input == 2 or user_input == 3:
            break
        else:
            print("Not an appropriate choice, try again.")


    # Convert user input to the corresponding option
    user_choice = rock_paper_scissors_options[user_input - 1]

    # Print the choices
    print(f"You chose: {user_choice} \nThe computer chose: {computer_choice}\n\n")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie! Let's try again!")
        tie += 1
        # Wait for the user to press Enter before continuing
        input("Press Enter to continue...")
        continue
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
        (user_choice == "Paper" and computer_choice == "Rock") or \
        (user_choice == "Scissors" and computer_choice == "Paper"):
        print("You win!")
        player_score += 1
        current_turn += 1
    else:
        print("The computer wins!")
        computer_score += 1
        current_turn += 1

    # Wait for the user to press Enter before continuing
    input("Press Enter to continue...")

clear_terminal()

print(f"Good game, thank you! \n\nFinal score:\n  -  You won {player_score} time(s)\n  -  Computer won {computer_score} time(s) and \n  -  There was/were tie(s) {tie} time(s).\n")