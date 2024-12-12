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

# 1/1. Kérj be a felhasználótól 4 programozási nyelvet
languages = input("Please enter 4 programming languages, separated by commas (no spaces): ").split(",")

# 1/2. Add hozzá a "skills" kulcs alatt
user_info["skills"] = languages

# 2. Rendezd a favourite_meals lista elemeit abc sorrendbe
user_info["favourite_meals"].sort()

# 3. Printeld ki a favourite_meals lista utolsó előtti elemét
print(f"The second last item in favourite_meals: {user_info['favourite_meals'][-2]}")

# 4. Adj hozzá egy “spaghetti” string-et a favourite_meals listához
user_info["favourite_meals"].append("spaghetti")

# 5. Add hozzá a favourite_meals harmadik és negyedik elemét újra
user_info["favourite_meals"].append(user_info["favourite_meals"][2])
user_info["favourite_meals"].append(user_info["favourite_meals"][3])

# 6. Töröld a duplikátumokat
user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))

# 7. Cseréld fel a favourite_meals első és utolsó elemét
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]

# 8. Adj hozzá egy új elemet a "phone_contacts"-hoz
user_info["phone_contacts"]["Lalika"] = "+36301112233"

# 9. Töröld a "Tim" entry-t, mert már nem él
del user_info["phone_contacts"]["Tim"]

# 10. Adj hozzá egy új embert, akinek 2 telefonszáma is van
user_info["phone_contacts"]["Dzsángó"] = ["+36701110000", "+36201112233"]

# Extra 1: Printeld ki a “skills” lista utolsó 3 elemét ellentétes sorrendben!
print(f"The last 3 skills in reverse order: {user_info['skills'][-3:][::-1]}")

# Extra 2: Tim2 átnevezése Tim-re
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")

# Végső eredmény kiíratása
pprint(user_info)
