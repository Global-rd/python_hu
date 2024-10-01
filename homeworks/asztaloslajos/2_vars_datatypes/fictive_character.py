"""
fictive_character.py --- Asztalos Lajos --- 2024.10.01
"""
from datetime import datetime, timedelta
#input
name = input("Név:")
age = int(input("Életkor"))
python_exp_in_years = int(input("Python tapasztalat(év)"))
#conversion
name = name.strip().title()
age_in_days = (datetime.today()-datetime.today().replace(year=datetime.today().year - age)).days
#print
print(f"My character is {age_in_days} old. His/her is {name} and he/she has {python_exp_in_years} years experience.")
