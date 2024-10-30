from os import system
from pprint import pprint

system("cls")

"""
1. Kérj be a felhasználótól 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül. 
2. Konvertáld a kapott stringet egy listává, és add hozzá a fenti dictionary-hez “skills” néven.
3. Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe.
    Printeld ki a favourite_meals lista utolsó előtti elemét
4. Adj hozzá egy “spaghetti” string-et ugyanehhez a listához.
5. Add hozzá a favourite_meals-hez az aktuális favourit_meals lista harmadik és negyedik elemét (nem az index-ét) újra.
6. Ezután töröld az így keletkezett duplikátumokat!
7. Cseréld fel a favourite_meals lista első és utolsó elemét!
8. A “phone_contacts” dictionary-hez adj hozzá egy új elemet, tetszőleges névvel és telefonszámmal.
9. Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts”-ban, viszont a "Tim" key mögött lévő 
telefonszám már nem él. Töröld ki a telefonkönyvből!
10. Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2 telefonszáma is van!

Extra 1: Printeld ki a “skills”  lista utolsó 3 elemét ellentétes sorrendben!
Extra 2: Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne átnevezni Tim2-t Tim-re!
"""

print("\nAnswer for the first question")
programming_languages = input(
    "Add 4 programming language types with comma separated: "
).split(",")

user_info = {
    "name": "Mike",
    "age": 25,
    "favourite_meals": ["pizza", "carbonara", "sushi"],
    "phone_contacts": {
        "Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+364005000",
    },
}

user_info["skills"] = programming_languages
pprint(user_info["skills"])


print("\nAnswer for the second and third questions")
# user_info["favourite_meals"] = sorted(user_info["favourite_meals"]) simplified for sorting
user_info["favourite_meals"].sort()
pprint(user_info["favourite_meals"][-2])
pprint(user_info["favourite_meals"])


print("\nAnswer for the fourth and fifth questions")
user_info["favourite_meals"].append("spaghetti")
# user_info["favourite_meals"].extend(["sushi", "spaghetti"]) hard coded version. Correct/better one in next line
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
pprint(user_info["favourite_meals"])


print("\nAnswer for the sixth question")
"""
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
user_info["favourite_meals"].sort() 
Set is not keeping in all cases the order. Next code line is a better solution to avoid 2 line coding
"""
user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))
pprint(user_info["favourite_meals"])


print("\nAnswer for the seventh question")
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = (
    user_info["favourite_meals"][-1],
    user_info["favourite_meals"][0],
)

pprint(user_info["favourite_meals"])


print("\nAnswer for the eight question")
user_info["phone_contacts"].update({"Andrew": "+46735716684"})
pprint(user_info["phone_contacts"])


print("\nAnswer for the nineth question")
del user_info["phone_contacts"]["Tim"]
pprint(user_info["phone_contacts"])


print("\nAnswer for the tenth question")
user_info["phone_contacts"].update({"Grzegorz": ["+46735716401", "+46735716499"]})
pprint(user_info["phone_contacts"])


print("\nAnswer for Extra question nr. 1")
pprint(user_info["skills"][-1:-4:-1])


print("\nAnswer for Extra question nr. 2")
phone_number_tim = user_info["phone_contacts"].pop("Tim2")
user_info["phone_contacts"]["Tim"] = phone_number_tim
pprint(user_info["phone_contacts"])
