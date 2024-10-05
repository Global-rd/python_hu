"""
Feladat 2: List és dictionary műveletek használata
Hozz létre egy user_info.py file-t, és kódold le a következő feladat megoldását. Nyugodtan használj kommenteket a különböző feladatpontok előtt, 
hogy később könnyedén átlásd hogy melyik sor milyen funkciót lát el.
Adott a következő dictionary, amely egy felhasználó adatai tartalmazza (másold át a kódodba):

user_info = {
    "name": "Mike",
    "age": 25,
    "favourite_meals": [
        "pizza",
        "carbonara",
        "sushi"
    ],
    "phone_contacts": {
        "Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+364005000"
    }
}

1,  Kérj be a felhasználótól 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül. Konvertáld a kapott stringet egy listává, 
    és add hozzá a fenti dictionary-hez “skills” néven. -- kész
2,  Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe. --kész
3,  Printeld ki a favourite_meals lista utolsó előtti elemét --kész
4,  Adj hozzá egy “spaghetti” string-et ugyanehhez a listához. --kész
5,  Add hozzá a favourite_meals-hez az aktuális favourit_meals lista harmadik és negyedik elemét (nem az index-ét) újra. -- kész
6,  Ezután töröld az így keletkezett duplikátumokat! -- kész
7,  Cseréld fel a favourite_meals lista első és utolsó elemét! -- kész
8,  A “phone_contacts” dictionary-hez adj hozzá egy új elemet, tetszőleges névvel és telefonszámmal. -- kész
9,  Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts”-ban, viszont a "Tim" key mögött lévő telefonszám már nem él. Töröld ki a telefonkönyvből! -- kész
10, Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2 telefonszáma is van! -- kész

Extra 1: Printeld ki a “skills”  lista utolsó 3 elemét ellentétes sorrendben!
Extra 2: Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne átnevezni Tim2-t Tim-re!
Tipp: Azoknál a feladatrészeknél amelyeknél ki kell printelni valamit, például az aktuális lista utolsó előtti elemét, nyugodtan printeld ki a teljes listát is mellé.
"""

from pprint import pprint

user_info = {
    "name": "Mike",
    "age": 25,
    "favourite_meals": [
        "pizza",
        "carbonara",
        "sushi"
    ],
    "phone_contacts": {
        "Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+364005000"
    }
}

prog_skills = input("What programming languages ​​do you know? Please give me 4 languages (separator ','):")
prog_skills_list = prog_skills.split(",")

user_info["skills"] = prog_skills_list #skills key feltöltődik prog_skills_list value-al

print(user_info["favourite_meals"])

user_info_sorted = sorted(user_info["favourite_meals"]) #az új sorrend bekerül a user_info_sorted változóba
user_info["favourite_meals"].sort() #a "favourite_meals"-t felülírjuk a user_info_sorted elemeivel
print(user_info["favourite_meals"])

print(user_info["favourite_meals"][-2])

user_info["favourite_meals"].append("spaghetti")

user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print(user_info["favourite_meals"])

user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]

user_info["phone_contacts"]["minime"] = "+3610234345"

del (user_info["phone_contacts"])["Tim"]
user_info["phone_contacts"]["Tim"] = (user_info["phone_contacts"]).pop("Tim2")

user_info["phone_contacts"]["ketteske"] = ["+3610234345","+3610234345"]

print(user_info["skills"][-1:-4:-1])

pprint(user_info)
