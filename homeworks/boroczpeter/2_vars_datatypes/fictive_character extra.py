#Second homework, task 1+extra

#asking for character informations
name = input ("Please give me your name: ").strip().upper()
age_years = int(input("How old are you? "))
python_exp_in_years = int(input("Your Python programming experience in years? "))
 #question of extra task
professional_developer = input("Do you want to be a profesional Python developer? (yes/no) ").strip().lower()

#calculate character age in days (asuming a year with 365 days )
age_in_days = age_years*365 #created a new variable

#using ternary operator in Boolean variable
want_to_be_dev = "wants" if professional_developer == "yes" else "does not want"

#interpolated string (f-string)
print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_exp_in_years} years experience. He/she {want_to_be_dev} to be a Python developer!")