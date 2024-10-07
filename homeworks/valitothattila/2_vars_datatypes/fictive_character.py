"""
Feladat 1: Változók, user input, string metódusok, type conversion, f-string használata
"""
#adatok bekérése
in_name = input("Enter your name: ")
in_age = input("How old are you: ")
in_python_exp_in_years = input("Years of Python experience: ")

#vizsgálatok
name = str.strip(in_name) #szóköz levágása elöl/hátul
name = str.capitalize(name) #leső betű legyen nagy
age_in_days = int(in_age)*365 #évek konvertálása napokká
python_exp_in_years = in_python_exp_in_years #csak a változó név "in_" miatt

#összefűzés
fictive_character = f'My character is {age_in_days} days old. His/her name is {name} and he/she has {python_exp_in_years} years experience.'

#kiírás
print(fictive_character)




