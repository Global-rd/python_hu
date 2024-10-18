'''
2. házi feladat

Feladat 2: List és dictionary műveletek használata

+ Extra 1 és 2 feladatok (szorgalmi)
'''

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../_0_Functions')))

from terminal_clearer import clear_terminal


from pprint import pprint

# Given dictionary
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

# 1. Ask the user to input 4 programming languages separated by commas, no spaces
languages = input("Enter 4 programming languages separated by commas, no spaces: ").split(',')

# Add the list to the dictionary under the key "skills"
user_info["skills"] = languages

'''
pprint(user_info)

Enter 4 programming languages separated by commas, no spaces: programming language1,programming language2,programming language3,programming language4
{'age': 25,
 'favourite_meals': ['pizza', 'carbonara', 'sushi'],
 'name': 'Mike',
 'phone_contacts': {'Jim': '+364005000',
                    'Mary': '+36701234567',
                    'Tim': '+36207654321',
                    'Tim2': '+36304567321'},
 'skills': ['programming language1',
            'programming language2',
            'programming language3',
            'programming language4']}
'''

# 2. Sort the "favourite_meals" list in ABC order
user_info["favourite_meals"].sort()

'''
pprint(user_info)

{'age': 25,
 'favourite_meals': ['carbonara', 'pizza', 'sushi'],
 'name': 'Mike',
 'phone_contacts': {'Jim': '+364005000',
                    'Mary': '+36701234567',
                    'Tim': '+36207654321',
                    'Tim2': '+36304567321'},
 'skills': ['programming language1',
            'programming language2',
            'programming language3',
            'programming language4']}
'''


# 3. Print the second to last element of the "favourite_meals" list
print(f"The second to last favourite meal is: {user_info['favourite_meals'][-2]}")

'''
 The second to last favourite meal is: pizza
'''

# 4. Add "spaghetti" to the "favourite_meals" list
user_info["favourite_meals"].append("spaghetti")

'''
print(user_info["favourite_meals"])

['carbonara', 'pizza', 'sushi', 'spaghetti']
'''

# 5. Add the third and fourth elements of the "favourite_meals" list again (not the index)
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

'''
print(user_info["favourite_meals"])

['carbonara', 'pizza', 'sushi', 'spaghetti', 'sushi', 'spaghetti']
'''

# 6. Remove duplicates from the "favourite_meals" list
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))

'''
print(user_info["favourite_meals"])

['carbonara', 'spaghetti', 'pizza', 'sushi']
'''

# 7. Swap the first and last elements of the "favourite_meals" list
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]

'''
print(user_info["favourite_meals"])

['carbonara', 'sushi', 'pizza', 'spaghetti']
'''

# 8. Add a new contact to "phone_contacts"
user_info["phone_contacts"]["Edit"] = "+36301234567"

'''
pprint(user_info["phone_contacts"])

{'Edit': '+36301234567',
 'Jim': '+364005000',
 'Mary': '+36701234567',
 'Tim': '+36207654321',
 'Tim2': '+36304567321'}
'''

# 9. Delete the "Tim" key from the "phone_contacts" dictionary
del user_info["phone_contacts"]["Tim"]

'''
pprint(user_info["phone_contacts"])

{'Edit': '+36301234567',
 'Jim': '+364005000',
 'Mary': '+36701234567',
 'Tim2': '+36304567321'}
'''

# 10. Add a new contact with 2 phone numbers to "phone_contacts"
user_info["phone_contacts"]["Mano"] = ["+36303334444", "+36201234567"]

'''
pprint(user_info["phone_contacts"])

{'Edit': '+36301234567',
 'Jim': '+364005000',
 'Mano': ['+36303334444', '+36201234567'],
 'Mary': '+36701234567',
 'Tim2': '+36304567321'}
'''

# EXTRA 1: Print the last 3 elements of the "skills" list in reverse order
if len(user_info["skills"]) >= 3:
    print("Last 3 skills in reverse order:", user_info["skills"][-3:][::-1])
else:
    print("Not enough skills to display the last 3 in reverse order.")

'''
Last 3 skills in reverse order: ['programming language4', 'programming language3', 'programming language2']
'''

# EXTRA 2: Rename "Tim2" to "Tim" in "phone_contacts"
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")

# Print the entire dictionary to see the changes
pprint(user_info)

'''
{'age': 25,
 'favourite_meals': ['sushi', 'carbonara', 'pizza', 'spaghetti'],
 'name': 'Mike',
 'phone_contacts': {'Edit': '+36301234567',
                    'Jim': '+364005000',
                    'Mano': ['+36303334444', '+36201234567'],
                    'Mary': '+36701234567',
                    'Tim': '+36304567321'},
 'skills': ['programming language1',
            'programming language2',
            'programming language3',
            'programming language4']}
'''