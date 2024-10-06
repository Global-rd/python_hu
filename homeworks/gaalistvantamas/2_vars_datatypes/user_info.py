"""
Author: Gaál István Tamás
Task: Homework-2 / 2 
"""
from pprint import pprint

# datas for task
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

# 1
programming_languages = str(input(
    "Please enter 4 programming languages! Without whitespaces and separeted by a comma!\n"))

programming_languages_list = list(programming_languages.split(","))
user_info["skills"] = programming_languages_list

print("\n1. exercise\n")
pprint(user_info)

# 2
user_info["favourite_meals"].sort()

print("\n2. exercise\n")
pprint(user_info)

# 3
print("\n3. exercise\n")
print(f"The second last element of the favourite meals is: {
    user_info["favourite_meals"][-2]}")

# 4
user_info["favourite_meals"].append("spagetthi")

print("\n4. exercise\n")
pprint(user_info)

# 5
user_info["favourite_meals"].append((user_info["favourite_meals"][2]))
user_info["favourite_meals"].append((user_info["favourite_meals"][3]))

print("\n5. exercise\n")
pprint(user_info)

# 6 
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))

print("\n6. exercise\n")
pprint(user_info)

# 7 
user_info["favourite_meals"].append((user_info["favourite_meals"][0]))
user_info["favourite_meals"][0] = ((user_info["favourite_meals"][-2]))
del (user_info["favourite_meals"][-2])

print("\n7. exercise\n")
pprint(user_info)

# 8 
user_info["phone_contacts"].update({"John": "+36708817890"})

print("\n8. exercise\n")
pprint(user_info)

# 9 
user_info["phone_contacts"].pop("Tim")

print("\n9. exercise\n")
pprint(user_info)

# 10 
user_info["phone_contacts"].update({"Tom": ["+36701234567", "+36301234567"]})

print("\n10. exercise\n")
pprint(user_info)

# +1 
print("\n+1. exercise\n")
print("The last 3 elements of the skills:", (user_info["skills"][:-4:-1]))

# +2 
print("\n+2. exercise\n")

user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")

pprint(user_info)
