name = input("What is your name? ").strip().title()
age = int(input("What is your age? "))
experience_in_Python = int(
    input("How many years of experience do you have in Python? ")
)
developper_desire = (
    input("Would you like to be a professional Python developper? Yes or no? ") == "yes"
)


age_in_days = age * 365


dev_intent = (
    "He wants to be a Python developer!"
    if developper_desire
    else "He does not want to be a Python developer!"
)
character_information = f"My character is {age_in_days} days old. \nHis name is {name} and he has {experience_in_Python} years experience. \n{dev_intent }"


print(character_information)
