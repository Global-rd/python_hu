"""
Feladat 1: Változók, user input, string metódusok, type conversion, f-string használata
Hozz létre egy fictive_character.py file-t, és kódold le a következő feladat megoldását:
Ebben a feladatban egy képzeletbeli karaktert fogsz létrehozni (mintázhatod nyugodtan magadról is :)). 
A feladatod, hogy a felhasználótól bekérd a következő input-okat (ezeknek megfelelő, leíró változóneveket adj):

Név:
Életkor:
Python tapasztalat években:

A tanultak alapján kódold le, hogy a beírt név minden esetben nagy betűvel legyen eltárolva a változóban, és szóköz se előtte, se utána ne szerepeljen.
Az életkort konvertáld át a megfelelő adattípusra, és egy új változóban tárold el hogy mennyi idős a karakter napokban 
(Kerekíts az években megadott életkor alapján, tételezzük fel hogy ma van az illető szülinapja).
Printeld ki az összes információt egy interpolált string-ben (f-string). A végeredmény valami ilyesmi kell hogy legyen:
 "My character is <age_in_days> old. His/her name is <name> and he/she has <python_exp_in_years> years experience."

Extra feladat (szorgalmi):
Kérd be inputként a felhasználótól, hogy szeretné-e hogy a karaktere profi Python fejlesztő legyen. Erre a válasz "yes" vagy "no" kell hogy legyen 
(az inputok validálást később tanuljuk). Nézz utána a ternary operator-oknak Python-ban, és tárold el ezt a változót egy boolean típusú változóban. 
Ezután add hozzá a végső kiprintelendő f-string-hez. A végeredménynek ekkor így kell kinéznie:

"My character is <age_in_days> old. His/her name is <name> and he/she has <python_exp_in_years> years experience. He/she wants to be a Python developer!"
Vagy
"My character is <age_in_days> old. His/her name is <name> and he/she has <python_exp_in_years> years experience. He/she does not want to be a Python developer!"
"""


name = input("What is your name? ")
name = name.strip().upper()

age = int(input("How old are you? "))
age_in_days = int(age * 365)

python_exp_in_years = int(input("Years of Python experience? "))

sex = str(input("She or He? "))
sex = sex.strip().upper()

python_dev = str(input("Years of Python experience? Yes or No? "))
python_dev = python_dev.strip().lower()


if  python_dev == "yes":
    python_dev_bool = True
elif python_dev == "no":
     python_dev_bool = False
else:
    print("Please answer Yes or NO!" )


if python_dev_bool == True:
    if sex == "HE":
        print(f"My character is {age_in_days} days old. His name is {name} and he has {python_exp_in_years} years experience.He wants to be a Python developer")
    else:
        print(f"My character is {age_in_days} days old. Her name is {name} and she has {python_exp_in_years} years experience.She wants to be a Python developer")
else:
    if sex == "HE":
        print(f"My character is {age_in_days} days old. His name is {name} and he has {python_exp_in_years} years experience.He does not want to be a Python developer!")
    else:
        print(f"My character is {age_in_days} days old. Her name is {name} and she has {python_exp_in_years} years experience.She does not want to be a Python developer!")
