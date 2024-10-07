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

# Programozási nyelvek bekérése
programming_languages = input("Adj meg 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül: ")

# String konvertálása listává
skills_list = programming_languages.split(",")

# Skills lista hozzáadása
user_info["skills"] = skills_list

# A 'favourite_meals' lista rendezése abc sorrendbe
user_info["favourite_meals"].sort()

# Print az utolsó előtti favourite meal-ről

print(user_info["favourite_meals"][-2])

# Add spaghetti

user_info["favourite_meals"].append("spaghetti")

# A harmadik és negyedik elem hozzáadása mégegyszer
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

# Dupla elemek eltávolítása
user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))

# Első és utolsó elem csere
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]

# Új telefon kontakt hozzáadása
user_info["phone_contacts"]["Máté"] = "+36706705649"

# "Tim" eltávolítása a telefonkönyvből
del user_info["phone_contacts"]["Tim"]

# Új kontakt hozzáadása két telefonszámmal
user_info["phone_contacts"]["Martin"] = ["+36703714301", "+36703714302"]

# Skills utolsó 3 eleme ellentétes sorrendben
last_three_skills = user_info["skills"][-3:][::-1]
print(last_three_skills)
print(user_info["skills"])

# Tim2 átnevezése Timre
if "Tim2" in user_info["phone_contacts"]:
    user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")

print(user_info)


