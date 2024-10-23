from pathlib import Path
import random
import json


def get_user_guess(interval_start: int, interval_end: int) -> int:

    """Asks the user for his/her current guess and returns it as an integer."""

    while True:
        try:
            guess = int(
                input(f"Guess a number between {interval_start} and {interval_end}: ")
            )
            if guess < interval_start or guess > interval_end:
                raise ValueError("Please enter a number within the range!")
            return guess
        except ValueError as e:
            print(f"Invalid input: {e}. Try again.")


def get_num_of_max_attempts() -> int:

    """Asks the user about how many attempts he/she would like to try to guess the number."""

    while True:
        try:
            num_of_attempts = int(input("How many guesses would you like to try? "))
            if num_of_attempts <= 0:
                raise ValueError("Please enter a positive number!")
            return num_of_attempts
        except ValueError as e:
            print(f"Invalid input: {e}. Try again.")


def play_game(interval_start: int, interval_end: int) -> None:

    """Main function to play the number guessing game."""

    print("Welcome to the Number Guessing Game!")
    target_number = random.randint(interval_start, interval_end)
    max_attempts = get_num_of_max_attempts()
    attempts = 0

    while attempts < max_attempts:
        guess = get_user_guess(interval_start=interval_start, interval_end=interval_end)
        attempts += 1

        if guess < target_number:
            print(f"Too low!")
        elif guess > target_number:
            print(f"Too high! ")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        print(f"You have {max_attempts - attempts} attempts left.")
    else:
        print(
            f"Sorry! You've used all {max_attempts} attempts. The number was {target_number}."
        )


def load_settings() -> dict:

    """Reads the settings containing the interval information."""
    
    settings_path = Path(__file__).parent / "settings.json"
    
    try:
        with settings_path.open("r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading settings: {e}, default values will be used for intervals.")
    
    return {}



