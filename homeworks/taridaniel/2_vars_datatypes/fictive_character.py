name_old = input("Please, enter your name: ")
name = name_old.strip().capitalize()

age = input("Please, enter your age: ")

python_exp_in_years = 2

age_in_days = int(age)*365
print(age_in_days)

print(f"My charater is {age_in_days} old. His name is {name} and he has {python_exp_in_years} years experience.")