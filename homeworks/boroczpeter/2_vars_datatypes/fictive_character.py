#Second homework, task 1

#asking for character informations
name = input ("Please give me your name: ").strip().upper()
age_years = int(input("How old are you? "))
python_exp_in_years = int(input("Your Python programming experience in years? "))

#calculate character age in days (asuming a year with 365 days ) in a different variable
age_in_days = age_years*365

#interpolated string (f-string)
print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_exp_in_years} years experience.")