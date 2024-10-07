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


#Exercise 1 - Asking for 4 programming langauges separated with comma without space. Converting the string to a list and adding it to the dictionary above
user_info["skills"] = input("Add 4 programming languages: ").split()

#Exercise 2 - Sorting the elements of favourite_meals list into alphabetical order
user_info["favourite_meals"].sort()

#Exercise 3 - Printing the second last element of favourite_meals list
print(user_info["favourite_meals"][-2])

#Exercise 4 - Adding spaghetti to favourite_meals list
user_info["favourite_meals"].append("spaghetti")

#Exercise 5 - Adding the 3rd and 4th element again to the current favourite_meals list
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])


#Exercise 6 - Deleting the recently created duplicates
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))

#Exercise 7 - Swapping the first and last element of favourite_meals
#Erre sajnos nem jöttem rá :(

#Exercise 8 - Adding a new element with name and phone number to phone_contacts
user_info["phone_contacts"].update({"Robert": "+36209876543"})

#Exercise 9 - Tim and Tim2 are the same people, delete Tim
user_info["phone_contacts"].pop("Tim")

#Exercise 10 - Add a new contact to phone_contacts list who has two different
user_info["phone_contacts"].update({"Bob": "+36209876543" "," "+36208765432"})

