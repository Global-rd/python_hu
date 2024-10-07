"""
Author: Gaál István Tamás
Task: Homework-2 / 1 
"""

DAYS_OF_A_YEAR = 365.25


# Ask for a name and convert
name = input("Please enter your name!\n").strip().title()

# Ask for an age and convert to days
age_in_years = int(input("Enter your age!\n"))

age_in_days = int(round(age_in_years * DAYS_OF_A_YEAR))


# Ask for years of experience
python_experience_in_years = int(
    input("How many years in python do you have?\n"))


# Based on the task specification
want_to_be_a_developer = input(
    "Do you want to be a Python developer? yes or no\n")

print(f"""\nMy charachter is {age_in_days} days old.
His/her name is {name} and he/she has {
    python_experience_in_years} {
    "year" if python_experience_in_years <= 1 else "years"} experience.
He/she {
    "wants" if want_to_be_a_developer == "yes" else "does not want"} to be a Python developer!\n""")
