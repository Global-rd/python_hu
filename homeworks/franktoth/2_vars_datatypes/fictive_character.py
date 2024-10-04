name = input("Enter your name: ")
age = int(input("Enter your age: "))
python_usage = int(input("How many years have you been using Python: "))
user_prof_dev = input("Do you want to be a professional Python developer? (yes/no)")

db_name = str.capitalize(name)  #captializing the name
db_name = str.strip(db_name)    #removing spaces
db_age_in_days = age*365        #calculation of days without leap years

prof_dev_decision = "He/She wants to be a prof Python Developer" if user_prof_dev=="yes" else "He/She doesn't want to be a prof developer"

print(f"My character is {db_age_in_days} days old.")
print(f"His/her name is {db_name}. He/she has {python_usage} years of Python experience.")
print(f"He/she has {python_usage} years of Python experience.")
print(prof_dev_decision)