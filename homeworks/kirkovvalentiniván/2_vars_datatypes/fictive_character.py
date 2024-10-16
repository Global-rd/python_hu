character_name = input("What is your character's name?  ").title().strip()  #Name input

character_age = int(input("How old is your character?  "))                  #Age input
character_age_days = character_age * 365                                    #Age input in days

python_exp = int(input("How many years of experience does he has in python programming? \
Please enter this using only numbers:  "))                                  #Experience input

python_learning_intention = input("Do you want to became an expert in python \
programming? (yes/no)  ").strip().lower()                                   #Learning intention input
answ_learn_intent = True if python_learning_intention == "yes" else False   #Boolean variable

#Output
introduction = f"My character is {character_age_days} days old. His name is \
{character_name} and he has {python_exp} years experience in python programming. \
He {"wants" if answ_learn_intent else "does not want"} to be a Python developer."

print(introduction)
