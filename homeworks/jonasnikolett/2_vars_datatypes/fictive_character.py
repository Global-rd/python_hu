"""Feladat 1: 
Változók, user input, string metódusok, type conversion, f-string használata
Hozz létre egy fictive_character.py file-t, és kódold le a következő feladat megoldását:
Ebben a feladatban egy képzeletbeli karaktert fogsz létrehozni (mintázhatod nyugodtan magadról is :)).
A feladatod, hogy a felhasználótól bekérd a következő input-okat (ezeknek megfelelő, leíró változóneveket adj):
    Név
    Életkor
    Python tapasztalat években
A tanultak alapján kódold le, hogy a beírt név minden esetben nagy betűvel legyen eltárolva a változóban, és szóköz se előtte, se utána ne szerepeljen.
Az életkort konvertáld át a megfelelő adattípusra, és egy új változóban tárold el hogy mennyi idős a karakter napokban 
(Kerekíts az években megadott életkor alapján, tételezzük fel hogy ma van az illető szülinapja).
Printeld ki az összes információt egy interpolált string-ben (f-string). 
A végeredmény valami ilyesmi kell hogy legyen: "My character is <age_in_days> old. His/her name is <name> and he/she has <python_exp_in_years> years experience."
"""

first_name = input("What is your first name?").strip().upper()

last_name = input("What is your last name?").strip().upper()

age = int(input("How old are you?"))
age_in_days = age * 365

python_experience_in_years = int(input("How many years of Python experience do you have? "))


 
print(f"My character is {age_in_days} days old. His/her name is {first_name} {last_name} and he/she has {python_experience_in_years} years experience.")






""""
Extra feladat (szorgalmi):
Kérd be inputként a felhasználótól, hogy szeretné-e hogy a karaktere profi Python fejlesztő legyen. Erre a válasz "yes" vagy "no" kell hogy legyen (az inputok validálást később tanuljuk). Nézz utána a ternary operator-oknak Python-ban, és tárold el ezt a változót egy boolean típusú változóban. Ezután add hozzá a végső kiprintelendő f-string-hez. A végeredménynek ekkor így kell kinéznie:
"My character is <age_in_days> old. His/her name is <name> and he/she has <python_exp_in_years> years experience. He/she wants to be a Python developer!"
Vagy
"My character is <age_in_days> old. His/her name is <name> and he/she has <python_exp_in_years> years experience. He/she does not want to be a Python developer!"
"""


python_developer_future = input("Do you want to be a professional Python developer in the future? Please answer briefley: Yes or No? ").strip().lower()

if  python_developer_future == "yes":
    python_developer_boolean = True
elif python_developer_future == "no":
     python_developer_boolean = False


if python_developer_boolean == True:
    developer_status_in_the_future = "wants"
else:
    developer_status_in_the_future = "does not want"

print(f"My character is {age_in_days} days old. His/her name is {first_name} {last_name} and he/she has {python_experience_in_years} years experience. He/she {developer_status_in_the_future} to be a Python developer!")

