
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

#1.

user_info["skills"] = input("Give me 4 programming languages which are separeted by comma!").split(",")


#2.

user_info["favourite_meals"].sort()

#3.

print(user_info["favourite_meals"][-2])

#4.

user_info["favourite_meals"].append("spaghetti")

#5.

user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
#6.

user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))

#7. 

user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]

#8.

user_info["phone_contacts"]["Jesus"] = "+363065484859"
print(user_info["phone_contacts"])

#9.

del user_info["phone_contacts"]["Tim"]

#10.

user_info["phone_contacts"]["Ismeretlen"] = ["+36705819657", "+36901234567"]

print(user_info)

#Extra 1.

print(user_info["skills"][:-4:-1])

#Extra 2.

if "Tim2" in user_info["phone_contacts"]:
    user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
    