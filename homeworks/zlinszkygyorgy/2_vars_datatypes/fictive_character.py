name = input("What is your name:")
age = input("What is your age:")
experience = input("Your python experience in years:")
developer = input("Do you want to be a Python developer? (yes/no)")

name = name.strip().capitalize()
age = int(age)
age = age * 365
pro_developer = developer.lower() == "yes"

introduction = f"My character is {age} days old. His/her name is {name} and he/she has {experience} years experience in python. He/she {'wants to be a Python developer' if pro_developer else 'doesnt want to be a Python developer'}."

print(introduction)