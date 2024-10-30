# Alapértelmezett dictionary
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

# Bekérjük a felhasználótól a programozási nyelveket
programming_languages = input("Adj meg 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül: ")

# Stringet listává konvertáljuk
skills = programming_languages.split(',')

# Hozzáadjuk a dictionary-hez 'skills' néven
user_info["skills"] = skills

# Kiírjuk a frissített dictionary-t
print("***************************************************")
print("Kiírjuk a frissített dictionary-t")
print(user_info)

# 2. Rendezd a favourite_meals lista elemeit abc sorrendbe
print("***************************************************")
print("Favourite_meals abc-be rendezés")
user_info['favourite_meals'].sort()
print(user_info)

# 3. Printeld ki a favourite_meals lista utolsó előtti elemét
print("***************************************************")
print("A favourite_meals lista utolsó előtti eleme:")
second_last_meal = user_info['favourite_meals'][-2]
print(second_last_meal)

# 4. Adj hozzá egy “spaghetti” string-et a listához
print("***************************************************")
print("Spaghetti hozzáadása: ")
user_info['favourite_meals'].append("spaghetti")
print(user_info)

# 5. Add hozzá a favourite_meals-hez a harmadik és negyedik elemet újra
print("***************************************************")
print("A harmadik és negyedik elemet újra hozzáadása")
if len(user_info['favourite_meals']) >= 4:
    user_info['favourite_meals'].extend([user_info['favourite_meals'][2], user_info['favourite_meals'][3]])
print(user_info)

# 6. Töröld az így keletkezett duplikátumokat
print("***************************************************")
print("A duplikátumok törlése :")
user_info['favourite_meals'] = list(dict.fromkeys(user_info['favourite_meals']))
print(user_info)

# 7. Cseréld fel a lista első és utolsó elemét
print("***************************************************")
print("Az első és utolsó elem cseréje")
user_info['favourite_meals'][0], user_info['favourite_meals'][-1] = user_info['favourite_meals'][-1], user_info['favourite_meals'][0]
print(user_info)

# 8. Adj hozzá egy új elemet a phone_contacts-hoz
print("***************************************************")
print("Új elem a phone_contact-hoz :")
user_info['phone_contacts']["John"] = "+36123456789"
print(user_info)

# 9. Töröld ki a "Tim" key-t
print("***************************************************")
print("Tim key törlés : ")
user_info['phone_contacts'].pop('Tim', None)
print(user_info)

# 10. Adj hozzá egy új embert, akinek két telefonszáma van
print("***************************************************")
print("Új ember hozzáadása : ")
user_info['phone_contacts']["Paul"] = ["+36201122334", "+36205566778"]
print(user_info)
print("***************************************************")
# Eredmény kiírása
print("Végeredmény : ")
print(user_info)

print("***************************************************")