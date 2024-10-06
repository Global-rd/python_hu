"""
Author: Gaál István Tamás
Task: Homework-2 / 1 
"""

DAYS_OF_A_YEAR = 365.25


# Ask for a name and convert
name = str(input("Please enter your name!\n"))

formated_name = name.strip().title()


# Ask for an age and convert to days
age_in_years = int(input("Enter your age!\n"))

age_in_days = int(round(age_in_years * DAYS_OF_A_YEAR))


# Ask for years of experience
python_experience_in_years = int(
    input("How many years in python do you have?\n"))


# Based on the task specification
want_to_be_a_developer = str(
    input("Do you want to be a Python developer? yes or no\n"))

want_to_become_a_developer = True if want_to_be_a_developer == "yes" else False


print(f"\nMy charachter is {age_in_days} days old.")
print(f"His/her name is {formated_name} and he/she has {
    python_experience_in_years} {
    "year" if python_experience_in_years <= 1 else "years"} experience.")
print(f"He/she {
    "wants" if want_to_become_a_developer else "does not want"} to be a Python developer!\n")
