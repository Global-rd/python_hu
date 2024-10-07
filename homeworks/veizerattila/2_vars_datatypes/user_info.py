# Feladat 2: List és dictionary műveletek használata
####################################################
import pprint as pp

# Dictionary létrehozása:
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

# 1. Kérj be a felhasználótól 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül. Konvertáld a kapott stringet egy listává, és add hozzá a fenti dictionary-hez “skills” néven.
print("1. Kérj be a felhasználótól 4 programozási nyelvet vesszővel elválasztva, szóközök nélkül.")
print("Konvertáld a kapott stringet egy listává, és add hozzá a fenti dictionary-hez “skills” néven!")
print("==========================================================================================================")
prog_skills = input("Give me 4 programming languages you're familiar with, separated by a comma! ")

if prog_skills.count(",")  == 3:
# Az if igaz ága csak akkor enged át, ha valaki 4 inputot adott meg, 3 vesszővel elválasztva

    skills = {"skills": prog_skills.split(",")}
    user_info.update(skills)

    pp.pprint(user_info)
    print("==========================================================================================================")


    # 2. Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe.
    keys = list(user_info.keys()) # kulcs változó definiálása, hogy így a dict. elemeire a key alapján k;s[bbi lehessen hivatkozni (pl.: "favourite_meals" helyett "2")
    user_info[keys[2]] = sorted(user_info[keys[2]])
    print("2. Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe!")
    pp.pprint(user_info)
    print("==========================================================================================================")


    # 3. Printeld ki a favourite_meals lista utolsó előtti elemét
    print("3. Printeld ki a favourite_meals lista utolsó előtti elemét!")
    pp.pprint(f"A 'favourite_meals' lista utolsó előtti eleme: {user_info[keys[2]][-2]}")
    print("==========================================================================================================")


    # 4. Adj hozzá egy “spaghetti” string-et ugyanehhez a listához.
    user_info[keys[2]].append("spaghetti")
    print("4. Adj hozzá egy “spaghetti” string-et ugyanehhez a listához!")
    pp.pprint(user_info)
    print("==========================================================================================================")


    # 5. Add hozzá a favourite_meals-hez az aktuális favourit_meals lista harmadik és negyedik elemét (nem az index-ét) újra.
    user_info[keys[2]].extend(user_info[keys[2]][2:3])
    print("5. Add hozzá a favourite_meals-hez az aktuális favourit_meals lista harmadik és negyedik elemét (nem az index-ét) újra!")
    print("megj.: a listának most nincs 4. eleme, a legutolsó elem a 3. index (most: 'spaghetti')")
    pp.pprint(user_info)
    print("==========================================================================================================")


    # 6. Ezután töröld az így keletkezett duplikátumokat!
    user_info[keys[2]] = sorted(list(dict.fromkeys(user_info[keys[2]]))) # itt újrarendeztem abc szerint
    print("6. Ezután töröld az így keletkezett duplikátumokat!")
    pp.pprint(user_info)
    print("==========================================================================================================")


    # 7. Cseréld fel a favourite_meals lista első és utolsó elemét! (Megj.: itt sem indexet használtam, hanem sima sorrendet.)
    ind1 , ind2 = 0 , -1
    user_info[keys[2]][0] , user_info[keys[2]][-1] = user_info[keys[2]][ind2] , user_info[keys[2]][ind1]
    print("7. Cseréld fel a favourite_meals lista első és utolsó elemét! (Megj.: itt sem indexet használtam, hanem sima sorrendet.)")
    pp.pprint(user_info)
    print("==========================================================================================================")


    # 8. A “phone_contacts” dictionary-hez adj hozzá egy új elemet, tetszőleges névvel és telefonszámmal!
    new_phone_contact = {"Mr Tajfel" : "+36707777777"}
    user_info["phone_contacts"].update(new_phone_contact)
    print("8. A “phone_contacts” dictionary-hez adj hozzá egy új elemet, tetszőleges névvel és telefonszámmal!")
    pp.pprint(user_info)
    print("==========================================================================================================")


    # 9. Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts”-ban, viszont a "Tim" key mögött lévő telefonszám már nem él. Töröld ki a telefonkönyvből!
    del user_info["phone_contacts"]["Tim"]
    print("9. Tim és Tim2 ugyanazt az embert reprezentálják a “phone_contacts”-ban, viszont a 'Tim' key mögött lévő telefonszám már nem él. Töröld ki a telefonkönyvből!")
    pp.pprint(user_info)
    print("==========================================================================================================")


    # 10. Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2 telefonszáma is van!
    new_phone_contact2 = {"Mr Grabowski" : ["+3620222222" , "+36201111111"]}
    user_info["phone_contacts"].update(new_phone_contact2)
    print("10. Adj hozzá egy olyan új embert “phone_contacts”-hoz, akinek 2 telefonszáma is van!")
    pp.pprint(user_info)
    print("==========================================================================================================")


    # Extra 1. Printeld ki a “skills”  lista utolsó 3 elemét ellentétes sorrendben!
    print("Extra 1. Printeld ki a “skills”  lista utolsó 3 elemét ellentétes sorrendben!")
    pp.pprint(user_info["skills"][:-4:-1])
    print("==========================================================================================================")


    # Extra 2. Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne átnevezni Tim2-t Tim-re!
    print("Most, hogy Tim-nek már csak 1 telefonszáma van, érdemes lenne átnevezni Tim2-t Tim-re!")
    user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"]["Tim2"]
    del user_info["phone_contacts"]["Tim2"]
    pp.pprint(user_info)
    print("==========================================================================================================")

else:
    print("You have to type exactly 4 programming skills. Please start over")