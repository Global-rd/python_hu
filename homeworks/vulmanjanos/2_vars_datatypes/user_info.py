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

program_languages = input("Mike, please give me 4 different program languages, seprated by a comma!")
print(program_languages)
program_language_list = program_languages.split(",") # listává konvertálás és elválasztás vesszővel
user_info.update({"skills": program_language_list}) # lista hozzáadása user infóhoz
user_info["favourite_meals"].sort() #lista abc sorrendbe rakása
pprint(user_info)
pprint(user_info["favourite_meals"][-2]) #az updatelt listáról az utolsó előtti elem kiírása
user_info["favourite_meals"].append("spagetthi") # hozzáadom a listához a spagetthit
pprint(user_info["favourite_meals"])
user_info["favourite_meals"].extend(["pizza", "sushi"]) # hozzáadom újra a pizzát és a sushit
pprint(user_info["favourite_meals"])
user_info["favourite_meals"].remove("pizza") # leszedem a pizzát
user_info["favourite_meals"].remove("sushi") # leszedem a sushit (2 elem elfogadása nem ment egyszerre a remove functionnal)
pprint(user_info["favourite_meals"])
new_user = {"Carl" : "+360301234567"} #new user létrehozása a phone contact hozzáadása előtt
user_info["phone_contacts"].update(new_user) # update a phone contactoknál a new userrel
pprint(user_info)
removed_value = user_info["phone_contacts"].pop("Tim") #Tim kitörlése a telefonkönyvből
user_info["phone_contacts"]["Roger"] = ["+36302134321", "+360217651234"] # update a phone contactoknál 2 telefonszámos userrel
pprint(user_info)