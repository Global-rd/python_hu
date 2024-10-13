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

# 1. input languages, add as skills to the dictionary
languages = input("Enter 4 programming languages (separated by commas, without spaces: ")
skills = languages.split(',')

user_info["skills"] = skills
pprint(user_info)

# 2. sort favorite meals by name ascending
user_info["favourite_meals"].sort()

# 3. print the penultimate item from favorite meals
print(user_info["favourite_meals"][-2])

# 4. add spaghetti to favourite meals
user_info["favourite_meals"].append("spaghetti")

# 5. add the 3. and 4. items of current favorite meals to the list again
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

# 6. delete the duplicates from favorite meals
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))

# 7. swap the first and last element of the favorite_meals list
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]

# 8. add new phone contact
user_info["phone_contacts"]["George"] = "+36304554551"

# 9. delete key 'Tim' from 'phone contacts'
del user_info["phone_contacts"]["Tim"]

# 10. add one new contact to 'phone contacts' with 2 separate phone numbers
user_info["phone_contacts"]["Erika"] = ["+36201234567", "+36301234567"]

# extra 1. print the last 3 items of skills in reversal order
print(user_info["skills"][-3:][::-1])

# extra 2. rename 'Tim2' to 'Tim'
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")


