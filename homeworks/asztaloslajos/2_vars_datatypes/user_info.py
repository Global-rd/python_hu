"""
user_info.py --- Asztalos Lajos --- 2024.10.01
"""
#data
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
#1
prg_languages = input("Add meg 4 programozási nyelv nevét vesszővel elválasztva:")
skills = prg_languages.split(",")
user_info["skills"] = skills
print(user_info["skills"])
#2
user_info["favourite_meals"].sort()
print(user_info["favourite_meals"])
#3
print(user_info["favourite_meals"][-2])
#4
user_info["favourite_meals"].append("spagetti")
print(user_info["favourite_meals"])
#5
user_info["favourite_meals"].append(user_info["favourite_meals"][2])
user_info["favourite_meals"].append(user_info["favourite_meals"][3])
print(user_info["favourite_meals"])
#6
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print(user_info["favourite_meals"])
#7
user_info["favourite_meals"][0],user_info["favourite_meals"][-1]=user_info["favourite_meals"][-1],user_info["favourite_meals"][0]
print(user_info["favourite_meals"])
#8
user_info["phone_contacts"]["John"]="+37 11 123 4566"
print(user_info["phone_contacts"])
#9
user_info["phone_contacts"]["Tim"]=None
print(user_info["phone_contacts"])
#10
user_info["phone_contacts"]["John2"]=["+36 1 356 4587", "+36 1 456 8914"]
print(user_info["phone_contacts"])
