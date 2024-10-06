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

skills_input = list((input("Enter 4 programming language, with commas,no spaces: ")).replace(" ","").split(",")) # replace szóköz ha mégis valaki szóközöket rakott volna, feltételezvén, h vesszőt rakott
#print(type(skills_input)) #check: sikerült-e listává konvertálni
user_info["skills"] = skills_input #adding new key and value input to dictionary
#print(user_info["skills"]) #check: sikerült-e hozzáadni a dictionary-hez skills-ként
user_info["favourite_meals"].sort()  # sorting favourite meals
print(user_info["favourite_meals"])  # tipp-print - teljes lista
print(user_info["favourite_meals"][-2]) # print - feladat not only check

user_info["favourite_meals"].append("spaghetti")  #a feladat nem kérte hogy újra sorba rendezzek, így nem teszem
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4]) # A 3. és 4. elemet adjuk hozzá (nem index)
#print(user_info["favourite_meals"]) #check
user_info["favourite_meals"] = list(set(user_info["favourite_meals"])) # keletkezett duplikáció elimination
#print(user_info["favourite_meals"]) #check
user_info["favourite_meals"][0] ,user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1] , user_info["favourite_meals"][0] #felcserélni az első és utolsó elemet
#print(user_info["favourite_meals"])  #check

user_info["phone_contacts"]["Andrew"]="+36707899876" #adding new member to phone_contacts
del user_info["phone_contacts"]["Tim"]     #Tim-et törölni

user_info["phone_contacts"]["Hubert"]=("+3630988866", "+3605559998") #adding new member to phone_contacts

print(user_info["skills"][-1::-1])   #skill utolsó 3 eleme fordított sorrendben

user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2") #Tim2-ből Tim-et csinálni

#pprint(user_info)


