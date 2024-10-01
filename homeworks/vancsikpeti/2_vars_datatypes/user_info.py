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

# Kérj be a felhasználótól 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül. 
#skills = list(input("Which four programming languages that do you know? (separate whit comma)").split(","))
skills = ["python","java","c+","php"]

# Konvertáld a kapott stringet egy listává, és add hozzá a fenti dictionary-hez “skills” néven.
user_info.update({"skills" : skills})

# Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe.
user_info["favourite_meals"].sort()

# Printeld ki a favourite_meals lista utolsó előtti elemét.
print(user_info["favourite_meals"][-2])

# Adj hozzá egy “spaghetti” string-et ugyanehhez a listához.
user_info["favourite_meals"].append("spagetti")

# Add hozzá a favourite_meals-hez az aktuális favourit_meals lista harmadik és negyedik elemét (nem az index-ét) újra
user_info["favourite_meals"].append(user_info["favourite_meals"][2])
user_info["favourite_meals"].append(user_info["favourite_meals"][3])

# Ezután töröld az így keletkezett duplikátumokat!
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))

# Cseréld fel a favourite_meals lista első és utolsó elemét!
first_favourite_meals = user_info["favourite_meals"][0]
last_favourite_meals = user_info["favourite_meals"][-1]
user_info["favourite_meals"][0] = last_favourite_meals
user_info["favourite_meals"][-1] = first_favourite_meals

# A “phone_contacts” dictionary-hez adj hozzá egy új elemet, tetszőleges névvel és telefonszámmal.
user_info["phone_contacts"].update({"Kenny":"+36301234567"})

# Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts”-ban, viszont a "Tim" key mögött lévő telefonszám már nem él. 
# Töröld ki a telefonkönyvből!
user_info["phone_contacts"].pop("Tim")

# Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2 telefonszáma is van!
user_info["phone_contacts"].update({"Stan": ["+36303451234","+35309876543"]})

# Extra 1: Printeld ki a “skills”  lista utolsó 3 elemét ellentétes sorrendben!
print(user_info["skills"])
print(user_info["skills"][-3:])
# !!! None ???

# Extra 2: Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne átnevezni Tim2-t Tim-re!
print(user_info["phone_contacts"].keys())
print(user_info["phone_contacts"].values())





