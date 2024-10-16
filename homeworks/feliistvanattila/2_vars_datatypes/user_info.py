# user_info.py

# Felhasználói adatok dictionary
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

# 1. Kérj be a felhasználótól 4 programozási nyelvet vesszővel elválasztva,
# szóközök nélkül. Konvertáld a kapott stringet egy listává,
# és add hozzá a fenti dictionary-hez “skills” néven.
skills_input = input("Kérlek add meg 4 programozási nyelvet, vesszővel elválasztva: ")

skills = []
for skill in skills_input.split(','):
    skills.append(skill.strip())

user_info["skills"] = skills

# 2. Rendezd a favourite_meals lista elemeit abc sorrendbe
user_info["favourite_meals"].sort()

# 3. Printeld ki a favourite_meals lista utolsó előtti elemét
print(f"A favourite_meals lista utolsó előtti eleme:{user_info['favourite_meals'][2]} ")

# 4. Adj hozzá egy "spaghetti" string-et a favourite_meals listához
user_info["favourite_meals"].append("spaghetti")

# 5. Add hozzá a favourite_meals-hez a harmadik és negyedik elemét újra
# Add hozzá a favourite_meals-hez az aktuális favourit_meals lista harmadik
# és negyedik elemét (nem az index-ét) újra.
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

# 6. Ezután töröld az így keletkezett duplikátumokat!
# TODO: Istvánt megkérdezni hogy erre mi a leghatékonyabb megoldás? Nincs valami olyan
# util könyvtár a List-nek hogy pl. RemoveDuplicates() 
# Nekem ez csak azért fura megoldás, mert nem implicit és aki nem ért phython-ul 
# annak lenet hogy nem egyértelmű itt hogy azért csinálunk set-et hogy 
# kiszedjük a duplikátumokat :)
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))

# 7. Cseréld fel a favourite_meals lista első és utolsó elemét
first_item = user_info["favourite_meals"][0]
last_item = user_info["favourite_meals"][-1]
user_info["favourite_meals"][0] = last_item
user_info["favourite_meals"][-1] = first_item

# 8. A “phone_contacts” dictionary-hez adj hozzá egy új elemet,
# tetszőleges névvel és telefonszámmal.
user_info["phone_contacts"]["Chris"] = "+36501234567"

# 10. Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts”-ban,
# viszont a "Tim" key mögött lévő telefonszám már nem él. 
# Töröld ki a telefonkönyvből!

print(f"Tömb a törlés előtt : {user_info['phone_contacts']}")
user_info["phone_contacts"].pop("Tim")
print(f"Tömb a törlés után : {user_info['phone_contacts']}")

# 11. Adj hozzá egy olyan új embert “phone_contacts”-hoz,
# akinek 2 telefonszáma is van!
print(f"Tömb tartalma hozzáadás előtt : {user_info['phone_contacts']}")
user_info["phone_contacts"]["Attes"] = ["+36601234567", "+36701234568"]
print(f"Tömb tartalma hozzáadás után : {user_info['phone_contacts']}")

# Az összes információ kiírása
print("\nFrissített felhasználói adatok:")
print(user_info)

# Extra 1: Printeld ki a “skills”  lista utolsó 3 elemét ellentétes sorrendben!
print(f"Tömb tartalma : {user_info['phone_contacts']}")
print(f"{user_info['skills'][-1:-4:-1]}")

# Extra 2: Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne átnevezni Tim2-t Tim-re!
print(f"Tömb tartalma módosítás előtt : {user_info['phone_contacts']}")
user_info["phone_contacts"]["Tim"] =  user_info["phone_contacts"].pop('Tim2')
print(f"Tömb tartalma módosítás után : {user_info['phone_contacts']}")


