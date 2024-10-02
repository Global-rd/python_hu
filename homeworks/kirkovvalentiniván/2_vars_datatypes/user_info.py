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

prog_language = input("List 4 programming languages. Separate them by comma without using space.")
prog_language_list = prog_language.split(",")
user_info["prog_language_list"] = prog_language_list
pprint(user_info)

sorted_favourite_meals = sorted(user_info["favourite_meals"])   #ABC sorba rendezés
pprint(sorted_favourite_meals)                                  #Új lista kiprintelése
print(sorted_favourite_meals[-2])                               #Új lista utolsó előtti eleme
sorted_favourite_meals.append("spaghetti")                      #Eredeti listához spaghetti hozzáadása
user_info["favourite_meals"].append("asd")
pprint user_info
