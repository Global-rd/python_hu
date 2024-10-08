name = input("What is your name:").strip().capitalize()
age = int(input("What is your age:"))
experience = input("Your python experience in years:")
developer = input("Do you want to be a Python developer? (yes/no)")

age = age * 365
pro_developer = developer.lower() == "yes"

introduction = f"My character is {age} days old.\
 His/her name is {name} and he/she has {experience} years experience in python.\
 He/she {'wants to be a Python developer' if pro_developer else 'doesnt want\
 to be a Python developer'}."

print(introduction)