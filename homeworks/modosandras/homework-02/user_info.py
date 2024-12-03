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

'''1. Kérj be a felhasználótól 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül. 
Konvertáld a kapott stringet egy listává, és add hozzá a fenti dictionary-hez “skills” néven.'''
languages = input("Adj meg 4 prog.nyelvet vesszővel elválasztva, szóközök nélkül.")
languages_list = languages.split(",")
print(languages_list)

user_info.update({"Skills":languages_list})
print(user_info)


'''2. Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe.'''
temp = user_info["favourite_meals"][0]
user_info["favourite_meals"][0] = user_info["favourite_meals"][1]
user_info["favourite_meals"][1] = temp

print(user_info)


'''3. Printeld ki a favourite_meals lista utolsó előtti elemét'''
print(user_info["favourite_meals"][-2])


'''4. Adj hozzá egy “spaghetti” string-et ugyanehhez a listához.'''
user_info["favourite_meals"].append("spaghetti")
print(user_info["favourite_meals"])


'''5. Add hozzá a favourite_meals-hez az aktuális favourit_meals lista 
harmadik és negyedik elemét (nem az index-ét) újra.'''

user_info["favourite_meals"].append(user_info["favourite_meals"][2])
user_info["favourite_meals"].append(user_info["favourite_meals"][3])
print(user_info["favourite_meals"])


'''6. Ezután töröld az így keletkezett duplikátumokat!'''
del user_info["favourite_meals"][4:]
print(user_info["favourite_meals"])


'''7. Cseréld fel a favourite_meals lista első és utolsó elemét!'''
temp = user_info["favourite_meals"][0]
user_info["favourite_meals"][0] = user_info["favourite_meals"][-1]
user_info["favourite_meals"][-1] = temp
print(user_info["favourite_meals"])


'''8. A “phone_contacts” dictionary-hez adj hozzá egy új elemet, 
tetszőleges névvel és telefonszámmal.'''
user_info["phone_contacts"]["Joe"] = "+36303334444"
print(user_info["phone_contacts"])


'''9. Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts”-ban, 
viszont a "Tim" key mögött lévő telefonszám már nem él. Töröld ki a telefonkönyvből!'''
del(user_info["phone_contacts"]["Tim"])
print(user_info["phone_contacts"])


'''10. Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2 telefonszáma is van!'''
user_info["phone_contacts"]["John"] = ["+36202223333", "+36707778888"]
print(user_info["phone_contacts"])



