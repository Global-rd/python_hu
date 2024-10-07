# Feladat 1: Változók, user input, string metódusok, type conversion, f-string használata
#########################################################################################

import datetime as dt # Dátumkezelési modul importálása, az age*365 helyett pontosabb napban számolt érték meghatározásához

# 1. Input által bekért változók definiálása:
name = input("What is your name? ").strip().title()
age = int(input("How old are you? "))
python_exp_in_years = int(input("Your Python experience (in years): "))
wannabe_dev_input = input("Do you want to be a Python developer? Type 'yes' or 'no': ")

# 2. Input értékek feldolgozása:
if wannabe_dev_input in ("yes", "no"): # csak "yes"/"no" elfogadása inputként, más érték esetén az else ágra ugrás

    wannabe_dev_insert = "wants" if wannabe_dev_input == "yes" else "doesn't want"   # Ternary operator alkalmazása és input tárolása boolean típusú változóként.

    this_date = dt.date.today()
    this_year = dt.date.today().year # születési dátum (éééé)
    this_month = dt.date.today().month
    this_day = dt.date.today().day
    birth_year = this_year - age
    birth_date = dt.date(birth_year, this_month, this_day)

    age_in_days = age * 365 #(this_date - birth_date).days
 
 # 3. Eredmény kiprintelése:
    print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_exp_in_years} years experience. He {wannabe_dev_insert} to be a PYthon developer.")
    #print(type(wannabe_dev_bool))

else:
    print("False input. Please start over and type 'yes' or 'no'")