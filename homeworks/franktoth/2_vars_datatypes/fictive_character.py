name = input("Enter your name: ").strip().capitalize()
age = int(input("Enter your age: "))
python_exp_in_years = int(input("How many years have you been using Python: "))
user_prof_dev = input("Do you want to be a professional Python developer? (yes/no)")

db_age_in_days = age*365        #calculation of days without leap years

prof_dev_decision = "He/She wants to be a prof Python Developer" if user_prof_dev=="yes" else "He/She doesn't want to be a prof developer"

print(f"My character is {db_age_in_days} days old.\n"
"His/her name is {name}. He/she has {python_exp_in_years} years of Python experience.\n"
"He/she has {python_exp_in_years} years of Python experience.\n"
"")
print(prof_dev_decision)