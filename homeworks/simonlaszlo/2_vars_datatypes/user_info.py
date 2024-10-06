
user_info={
    "name":"Mike",
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
skills_in = input("Kerek 4 programozasi nyelvet, vesszővel elválasztva, szóközök nélkül: ") # 1. adatbekeres
user_info["skills"]=(skills_in.split(","))
#print(user_info["skills"])

user_info["favourite_meals"].sort() # 2. sorbarendezes
#print(user_info["favourite_meals"])

print(user_info["favourite_meals"]) # 3. az utolso elotti elem
print(user_info["favourite_meals"][-2])

user_info["favourite_meals"].append("spaghetti") # 4. elem hozzaadasa
#print(user_info["favourite_meals"])

user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4]) # 5. ket elem hozzaadasa
#print(user_info["favourite_meals"])

user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"])) # 6. duplikacio torles
#print(user_info["favourite_meals"])

user_info["favourite_meals"].append(user_info["favourite_meals"][0]) # 7. elemek felcserelese
user_info["favourite_meals"][0]=(user_info["favourite_meals"][-2])
user_info["favourite_meals"].pop(3)
#print(user_info["favourite_meals"])

user_info["phone_contacts"]["Programmer"]="+36203263829" # 8. uj elem hozzaadas
#print(user_info["phone_contacts"])

user_info["phone_contacts"].pop("Tim",None) # 9. kulcs torlese
#print(user_info["phone_contacts"])

user_info["phone_contacts"]["Architect"]=["+36203263929","+36703263929"]# 10. uj kulcs hozzaadas
#print(user_info["phone_contacts"]["Architect"])

print(user_info["skills"]) # +1 az utolso 3 elem ellentetes sorrendben
print(user_info["skills"][-3:][-1::-1])

user_info["phone_contacts"]["Tim"]=user_info["phone_contacts"]["Tim2"] # +2 Tim atnevezese
user_info["phone_contacts"].pop("Tim2",None)
#print(user_info["phone_contacts"])