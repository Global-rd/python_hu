name = input("Név: ").strip().capitalize()
age = int(input("Életkor: "))
experience = input("Python tapasztalat: ")

#name = name.strip().capitalize()

#age = int(age)

age_in_days = age * 365

print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {experience} years experience with Python.")
