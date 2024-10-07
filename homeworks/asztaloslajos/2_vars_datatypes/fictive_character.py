"""
fictive_character.py --- Asztalos Lajos --- 2024.10.01
modified at 2024.10.05
"""
#input
name = input("Név:").strip().title()
age = int(input("Életkor"))
python_exp_in_years = int(input("Python tapasztalat(év)"))
#conversion
age_in_days = age*365
#print
print(f"My character is {age_in_days} old. His/her name is {name} and he/she has {python_exp_in_years} years experience.")
