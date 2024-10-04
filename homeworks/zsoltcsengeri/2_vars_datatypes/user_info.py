from pprint import pprint

# The dictionary
user_info = {
    "name": "Mike",
    "age": 25,
    "favourite_meals": ["pizza", "carbonara", "sushi"],
    "phone_contacts": {
        "Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+364005000",
    },
}


# 1 Request 4 programming languages from the user (comma-separated)
programming_languages = input(
    "Please give me 4 programming languages comma-separated: "
)

print(type(programming_languages))

# Convert input string to a list. Another method to convert to list is to use list() function:list(programming_languages)
programming_languages_list = programming_languages.split(",")
print(programming_languages_list)
print(type(programming_languages_list))

# Add 'skills' key to user_info dictionary
user_info["skills"] = programming_languages_list
pprint(user_info)

# 2 Sort the favourite_meals list alphabetically
user_info["favourite_meals"].sort()
pprint(user_info)

# 3 Print the sorted list and the second-to-last element
print(user_info["favourite_meals"][-2])

# 4 Add 'spaghetti' to favourite_meals
user_info["favourite_meals"].append("spaghetti")
print(user_info["favourite_meals"])
pprint(user_info)

# 5 Add the 3rd and 4th elements again to favourite_meals (based on current list)
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
print(user_info["favourite_meals"])

# 6 Remove duplicates (note: set() removes duplicates but changes order)
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))
print(user_info["favourite_meals"])

# 7 Swap the first and last elements of favourite_meals
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]
pprint(user_info)

# 8 Add a new contact to phone_contacts
user_info["phone_contacts"]["Zsolt"] = "07735283347"
pprint(user_info)

# 9 Remove Tim's old number (set the number to an empty string)
user_info["phone_contacts"]["Tim"] = ""
pprint(user_info)

# 10 Add a new contact with two phone numbers
user_info["phone_contacts"]["Zsolt2"] = ["07735636985", "07735874521"]
pprint(user_info)

# Extra 1: Print the last 3 skills in reverse order
print(user_info["skills"][-3:])

# Extra 2: Rename 'Tim2' to 'Tim'
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
pprint(user_info)
