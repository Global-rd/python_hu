name = input("Whats your name?\n").upper().strip()
age = int(input("How old are you?\n"))
age_in_days = age * 365 
python_exp_in_years = int(input("How many years do you have in python?\n"))

introduction = f"My carachter is {age} old. His name is {name} and he has {python_exp_in_years} experience."
print(introduction)
