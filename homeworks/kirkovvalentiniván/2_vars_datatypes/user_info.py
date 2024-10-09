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

prog_language = input("List 4 programming languages. Separate them by comma without using space.")  #1a Ask for 4 programming languages
prog_language_list = prog_language.split(",")                                                       #1b Conversion to lists
user_info["skills"] = prog_language_list                                                            #1c List adding to dictionaries
pprint(user_info)
user_info["favourite_meals"].sort()                                                                 #2. Sorting to alphabetical order
pprint(user_info)
print(user_info["favourite_meals"][-2])                                                             #3. Printing the penultimate element

user_info["favourite_meals"] += ["spaghetti"]                                                       #4. Adding spaghetti to the original list

user_info["favourite_meals"] += user_info["favourite_meals"][2:4]                                   #5. Appending the 3rd and 4th element of the list to favourite_meals 

user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))                              #6. Deleting the dupplications

user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = \
user_info["favourite_meals"][-1], user_info["favourite_meals"][0]                                   #7. Swithcing the first and last element of favourite_meals 

user_info["phone_contacts"].update(Jake="+36307683442")                                             #8. Appending one additional element to phone_contacts

user_info["phone_contacts"].pop("Tim")                                                              #9. Popping Tim from phone_contacts

user_info["phone_contacts"]["Lauren"] = ["+36708792632", "+36209847284"]                            #10. Adding a new person to phone_contacts with a list including 2 phone numbers
pprint(user_info["phone_contacts"])

print(user_info["skills"][-3:][::-1])                                                               #+1 Print the last 3 values of skills in an opposite order
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")                        #+2 Change Tim2 to Tim

pprint(user_info)