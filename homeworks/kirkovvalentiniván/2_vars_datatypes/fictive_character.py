character_name = input("What is your character's name?  ").title().strip()

character_age = int(input("How old is your character?  "))
character_age_days = round(character_age * 365, 0) 

python_exp = int(input("How many years of experience does he has in python programming? \
Please enter this using only numbers:  "))

python_learning_intention = input("Do you want to became an expert in python programming? (yes/no)  ").strip().lower()
answ_learn_intent = True if python_learning_intention == "yes" else False


introduction = f"My character is {character_age} years old. His name is \
{character_name} and he has {python_exp} years experience in python programming.\
He {"wants" if answ_learn_intent else "does not want"} to be a Python developer."

print(introduction)
