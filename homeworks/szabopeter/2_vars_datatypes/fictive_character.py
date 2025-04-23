#adatok bekérése
your_name = input("What's your name?")
your_age = int(input("What's your age?"))
python_exp_in_years = int(input("How long have you been learning Python? (Please enter a whole number, example: 10)"))
python_developer = (input("Would you like become a Python developer? Yes or No?"))

your_name = your_name.strip().title()
python_developer = python_developer.strip().lower()
your_age_in_days = your_age * 365
python_developer = True if python_developer == "yes" else False

if python_developer:
    print(f"Hello, your name is {your_name} and you're {your_age} years old. You've a {python_exp_in_years} year(s) Python experiences, which is really nice! You wants to be a pro Python developer. That's great!")
else:
    print(f"Hello, your name is {your_name} and you're {your_age} years old. You've a {python_exp_in_years} year(s) Python experiences, which is really nice! Sadly, you doesn't want to be a pro Python developer.")