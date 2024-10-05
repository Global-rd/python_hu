import pprint


#Original Dictionary
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



#1. programming languages#
programming_languages_correctable = input ("Write 4 programming language: ").strip()
programming_languages = ",".join(programming_languages_correctable.split()) #szóközök eltávolítása, és szavak vesszővel elválasztása#

skills = programming_languages.split(",") #listává alakítás

user_info["skills"] = (skills) #"skills" value/key páros létrehozása

#2. Sorba rendezés

user_info["favourite_meals"].sort()  #sorba rendezés

#3. Utolsó előtti elem printelése
print(user_info["favourite_meals"])
print(user_info["favourite_meals"][-2])


#4. Spaghetti hozzáadása
user_info["favourite_meals"].extend(["spaghetti"])


#5. favourite_meals listához hozzáadni az aktuális favourit_meals lista 3. 4. elemét újra
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])


#6. Duplikátumok törlése
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))


#7. favourite_meals lista első és utolsó elemének felcserélése
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]


#8. A “phone_contacts” dictionary-hez adj hozzá egy új elemet, tetszőleges névvel és telefonszámmal.
user_info["phone_contacts"]["Ronald"] = "+36709876521"


#9 Tim törlése
del user_info["phone_contacts"]["Tim"]

#10 Új ember 2 telefonszámmal
user_info["phone_contacts"]["Desmond"] = ["+36709876521", "+36709876533"]


#+1  Printeld ki a “skills”  lista utolsó 3 elemét ellentétes sorrendben!
print(user_info["skills"][-3:][::-1])


#+2 Tim2 átnevezése Tim-re
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")

print(user_info["phone_contacts"])