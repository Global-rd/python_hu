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
# 1. add programing languages 

user_info["skills"] = input("Give me 4 programming languages seperated by comma!\n").split(",")

# 2. ordering favorite meals

user_info["favourite_meals"].sort()

# 3. print openultimate element

print(user_info["favourite_meals"][-2])

# 4. add spagetti

user_info["favourite_meals"].append("spaghetti")

# 5. add third fourth element again

user_info["favourite_meals"].extend([user_info["favourite_meals"][2], user_info["favourite_meals"][3]])
pprint(user_info)

# 6. remove duplicates

user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))


# 7. swap first and last elements

user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0] 


# 8. add new contact

user_info["phone_contacts"]["Zsóka"] = "+7012345678"


# 9. remove Tim from contact

del user_info["phone_contacts"]["Tim"]


# 10. add contact with two numbers

user_info["phone_contacts"]["Lajos"] = ["+709876543","+301264366"]
