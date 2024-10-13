"""
Feladat 2: List és dictionary műveletek használata
"""
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

"2/1. feladat"
print("-----------------------1---------------------------")
prog_language = input("Give me 4 programing languge separated by a comma!")
skills_list = prog_language.split(",") #adatok konvertálása listába
user_info["skills"]=skills_list #lista hozzádása dictionray-hez
print(user_info)

"2/2. feladat"
print("-----------------------2---------------------------")
user_info["favourite_meals"].sort() #abc szerinti növekvő sorrend
print(user_info["favourite_meals"])

"2/3. feladat"
print("-----------------------3---------------------------")
print(user_info["favourite_meals"][-2]) #favourite_meals lista utolsó előtti elemét

"2/4. feladat"
print("-----------------------4---------------------------")
user_info["favourite_meals"].append("spaghetti") #Hozzá ad egy “spaghetti” string-et ugyanehhez a listához
print(user_info["favourite_meals"])

"2/5. feladat"
print("-----------------------5---------------------------")
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4]) # Hozzá adja a favourite_meals-hez az aktuális favourit_meals lista harmadik és negyedik elemét
print(user_info["favourite_meals"])

"2/6. feladat"
print("-----------------------6---------------------------")
user_info["favourite_meals"] = list(set(user_info["favourite_meals"])) #  Törli az így keletkezett duplikátumokat
print(user_info["favourite_meals"])

"2/7. feladat"
print("-----------------------7---------------------------")
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
#felcseréli a favourite_meals lista első és utolsó elemét
print(user_info["favourite_meals"])

"2/8. feladat"
print("-----------------------8---------------------------")
user_info["phone_contacts"]["Attila"] = "+36304469338" #A “phone_contacts” dictionary-hez ad hozzá egy új elemet, névvell és telefonszámmal
print(user_info["phone_contacts"])

"2/9. feladat"
print("-----------------------9---------------------------")
del user_info["phone_contacts"]["Tim"] #Tim key törlése
print(user_info["phone_contacts"])

"2/10. feladat"
print("----------------------10---------------------------")
user_info["phone_contacts"]["Béla"] = ["+36303812246", "+36302273641"] #Új ember hozzáadása 2 db telefonszámmal
print(user_info["phone_contacts"])





