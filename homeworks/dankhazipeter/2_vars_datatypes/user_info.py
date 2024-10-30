# Adott dictionary
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

# 1. Kérj be a felhasználótól 4 programozási nyelvet
programming_languages = input(
    "Adj meg 4 programozási nyelvet vesszővel elválasztva, szóköz nélkül: ")
skills_list = programming_languages.split(",")

# Ellenőrizzük, hogy pontosan 4 elemet kaptunk-e
if len(skills_list) != 4:
    # Ezt kérdeztem órán, mint early return, de mivel ez nem egy függvény, így valóban nincs értelme
    # Nem szeretném az egész további kódot indentálni, ezért itt kilépek, ha nem megfelelő a bemenet
    # Természetesen átírom, ha ez a módszer nem megfelelő
    raise ValueError("Pontosan 4 programozási nyelvet kell megadnod!")

# szóköz nélkül kérem a felsorolást, de ezt nem ellenőrzöm, ezért lehet ilyen eredmény, de ezzel most nem foglalkozom
# pl. "Python, Java, C++, JavaScript" -> ["Python", " Java", " C++", " JavaScript"]
user_info["skills"] = skills_list
print("Skills:", user_info["skills"])

# 2. Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe
user_info["favourite_meals"].sort()
print("Favourite meals ABC sorrendben:", user_info["favourite_meals"])

# 3. Printeld ki a favourite_meals lista utolsó előtti elemét
print("Favourite meals utolsó előtti eleme:", user_info["favourite_meals"][-2])

# 4. Adj hozzá egy "spaghetti" string-et a favourite_meals-hez
user_info["favourite_meals"].append("spaghetti")
print("Favourite meals spaghetti hozzáadása után:",
      user_info["favourite_meals"])

# 5. Add hozzá a favourite_meals-hez a harmadik és negyedik elemet újra
third_meal = user_info["favourite_meals"][2]
fourth_meal = user_info["favourite_meals"][3]
user_info["favourite_meals"].extend([third_meal, fourth_meal])
print("Favourite meals duplikált elemekkel:", user_info["favourite_meals"])

# 6. Töröld a duplikátumokat a favourite_meals-ből
user_info["favourite_meals"] = list(
    dict.fromkeys(user_info["favourite_meals"]))
print("Favourite meals duplikátumok törlése után:",
      user_info["favourite_meals"])

# 7. Cseréld fel a favourite_meals lista első és utolsó elemét
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
print("Favourite meals első és utolsó elem felcserélése után:",
      user_info["favourite_meals"])

# 8. Adj hozzá egy új elemet a "phone_contacts" dictionary-hez
user_info["phone_contacts"]["Anna"] = "+36204223433"
print("Phone contacts új elemmel:", user_info["phone_contacts"])

# 9. Töröld a "Tim" key-t a "phone_contacts"-ből
user_info["phone_contacts"].pop("Tim")
print("Phone contacts Tim törlése után:", user_info["phone_contacts"])

# 10. Adj hozzá egy olyan embert "phone_contacts"-hoz, akinek 2 telefonszáma is van
user_info["phone_contacts"]["Steve"] = ["+36701231234", "+36709876543"]
print("Phone contacts Steve 2 telefonszámmal:", user_info["phone_contacts"])

# Extra 1: Printeld ki a "skills" lista utolsó 3 elemét ellentétes sorrendben
print("Skills lista utolsó 3 eleme ellentétes sorrendben:",
      user_info["skills"][-3:][::-1])

# Extra 2: Tim2 átnevezése Tim-re
# Így az utolsó helyre kerül az új Tim, remélem ez nem gond, a feladat nem mondta, hogy ugyanarra a helyre
# Ahogy rákerestem, nem olyan egyszerű kulcsot átnevezni
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
print("Phone contacts Tim2 átnevezése Tim-re:", user_info["phone_contacts"])
