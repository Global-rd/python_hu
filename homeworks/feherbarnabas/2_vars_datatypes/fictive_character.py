name = str(input("What is your name? "))
name = name.strip().capitalize()

age = int(input("How old are you? "))
age_in_days = age * 365

python_exp_in_years = int(input("How many years of experience do you have in Python? "))

details_about_character = f"My character is {age_in_days} days old. His/her name is {name} and she/he has {python_exp_in_years} years experience."

answer = input("Would you like to be a Python developer? (yes/no): ").strip()
details_about_character += " He/she wants to be a Python developer!" if answer == "yes" else " He/she does not want to be a Python developer!"

print(details_about_character) 