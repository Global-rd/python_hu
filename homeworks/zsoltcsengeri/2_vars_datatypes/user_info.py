from pprint import pprint

# The dictionary
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


# 1 Kérj be a felhasználótól 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül.
programming_languages = input(
    "Please give me 4 programming languages comma separated: "
)

print(type(programming_languages))

programming_languages_list = programming_languages.split(",")
# Konvertáld a kapott stringet egy listává. Another method to convert to list is to use list() function:list(programming_languages)
print(programming_languages_list)
print(type(programming_languages_list))
# add hozzá a fenti dictionary-hez “skills” néven
user_info["skills"] = programming_languages_list

pprint(user_info)
user_info["favourite_meals"]
# Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe.
sorted_favourite_meals = sorted(user_info["favourite_meals"])

pprint(sorted_favourite_meals)

# Printeld ki a favourite_meals lista utolsó előtti elemét
print(user_info["favourite_meals"][-2])

# Adj hozzá egy “spaghetti” string-et ugyanehhez a listához.
user_info["favourite_meals"].append("spaghetti")
print(user_info["favourite_meals"])
pprint(user_info)

# Add hozzá a favourite_meals-hez az aktuális favourit_meals lista harmadik és negyedik elemét (nem az index-ét) újra.
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print(user_info["favourite_meals"])

# Ezután töröld az így keletkezett duplikátumokat!
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print(user_info["favourite_meals"])

# Cseréld fel a favourite_meals lista első és utolsó elemét!

# A “phone_contacts” dictionary-hez adj hozzá egy új elemet, tetszőleges névvel és telefonszámmal.

user_info["phone_contacts"]["Zsolt"] = "07735283347"
pprint(user_info)

# Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts”-ban, viszont a "Tim" key mögött lévő telefonszám már nem él. Töröld ki a telefonkönyvből!
user_info["phone_contacts"]["Tim"] = ""
pprint(user_info)

# Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2 telefonszáma is van!
user_info["phone_contacts"]["Zsolt2"] = ["07735636985", "07735874521"]
pprint(user_info)

# 1,2,3,4Extra 1: Printeld ki a “skills”  lista utolsó 3 elemét ellentétes sorrendben!
print(user_info["skills"][-3:])

#Extra 2: Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne átnevezni Tim2-t Tim-re!
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
pprint(user_info)