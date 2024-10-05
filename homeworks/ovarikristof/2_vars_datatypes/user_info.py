from pprint import pprint

user_info = {
    "name": "Mike",
    "age": 25,
    "favourite_meals": 
        ["pizza",
        "carbonara",
        "sushi"],
    "phone_contacts": 
        {"Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+364005000"}
 }


#1. BEKÉRÜNK 4 DARAB PROGRAMOZÁSI NYELVET.
programing_language = [(input("Please enter four programing language with comma and without spaces between the words." ))]


#2. HOZZÁADJUK A DICTIONARYHEZ A BEKÉRT ADATOT "SKILLS" KEY-KÉNT
user_info["skills"] = programing_language

print(user_info)


#3. FAVOURITE_MEALS RENDEZÉSE ABC SORRENDBEN.
sorted_by_meals = sorted(user_info["favourite_meals"])

print(sorted_by_meals)


#4. SPAGETTHI STRING HOZZÁADÁSA A LISTÁHOZ.
user_info["favourite_meals"].append("spaghetti")         

sorted_by_meals = sorted(user_info["favourite_meals"])

print(sorted_by_meals)


#5. FAVOURITE_MEALS 3. ÉS 4. ELEMÉT HOZZÁADJUK A FAVOURITE_MEALS LISTÁHOZ.
user_info["favourite_meals"].append(user_info["favourite_meals"][2])
user_info["favourite_meals"].append(user_info["favourite_meals"][3])


#6. DUPLIKÁCIÓKAT ELTÁVOLÍTJUK
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))



#7. FELCSERÉLJÜK A FAVOURITE_MEALS ELSŐ ÉS UTOLSÓ TAGJÁT.
first_meal = user_info["favourite_meals"][0]
last_meal = user_info["favourite_meals"][-1]                # Az első és utolsó tétel kiválasztása

user_info["favourite_meals"][0] = last_meal
user_info["favourite_meals"][-1] = first_meal               # Felcseréljük az első és utolsó tételt a listában

print(user_info["favourite_meals"])


#8. PHONE_CONTACTS-HOZ HOZZÁADUNK EGY ÚJ ELEMET.
user_info["phone_contacts"]["Adam"] = "+36304567341"


#9. TIM ÉS TIM2 UGYANAZ A SZEMÉLY TIM TELEFONSZÁMA MEGSZŰNT KISZEDJÜK A LISTÁBÓL.
user_info["phone_contacts"]["Tim"] = None


#10. EGY SZEMÉLY HOZZÁADÁSA, AKINEK 2 DARAB TELEFONSZÁMA VAN.
user_info["phone_contacts"]["Daniel"] = ["+36203495863","+36309412401"]


print("------------------")


pprint(user_info)
