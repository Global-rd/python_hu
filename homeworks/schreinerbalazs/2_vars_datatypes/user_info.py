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

#1 Ask the user for input
languages = input("Please enter 4 programming languages, separated by commas, without spaces: ")
# Convert the input string to a list
user_info.update({"skills":languages.split(",")})

#2 favourite_meals lista elemeit abc szerint 
user_info["favourite_meals"].sort()
pprint(user_info)

#3 favourite_meals lista utolsó előtti elem
print(user_info["favourite_meals"][-2])

#4 “spaghetti” string
user_info["favourite_meals"].append("spaghetti")
#print(user_info["favourite_meals"])

#5 Add hozzá a favourite_meals-hez az aktuális favourit_meals lista harmadik és negyedik elemét (nem az index-ét) újra.
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

#6 Ezután töröld az így keletkezett duplikátumokat!
user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))
# print(user_info["favourite_meals"])

#7 Cseréld fel a favourite_meals lista első és utolsó elemét!
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
# print(user_info["favourite_meals"])

#8 A “phone_contacts” dictionary-hez adj hozzá egy új elemet
user_info["phone_contacts"]["Jenő"] = "+36701111111"
# print(user_info["phone_contacts"])

#9 Töröld ki a telefonkönyvből!
del user_info["phone_contacts"]["Tim"]
# print(user_info["phone_contacts"])

#10 Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2 telefonszáma is van!
user_info["phone_contacts"]["Ferenc"] = ["+36702222222", "+36703333333"]
# print(user_info["phone_contacts"])

# E1
print(user_info["skills"][-3:][::-1])

# E2
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop ("Tim2")
# print(user_info["phone_contacts"])

#Ell
pprint (user_info)