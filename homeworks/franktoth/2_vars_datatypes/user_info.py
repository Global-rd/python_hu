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

lang_entry = input("Please enter 4 programming language with comma separators:")
lang_list = lang_entry.split(",")
user_info["Skills"] = lang_list              #adding the language skill to the user info
user_info["favourite_meals"].sort()                 #meals entries are sorted in ABC order
print(user_info["favourite_meals"][-2])             #last but 1 entry print of the meals list
user_info["favourite_meals"].append("spaghetti")    #adding spaghetti to favourites
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4]) #once more the 3rd and 4th meals to fav meals
user_info["favourite_meals"] = list(set(user_info["favourite_meals"])) #deleting the dupliactes by conevrting to set
user_info["favourite_meals"][0], user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1], user_info["favourite_meals"][0]   #exchange the first and last values of the fav meals list
user_info["phone_contacts"]["Frank"] = "+3655512345"    #new entry to phone contacts
del user_info["phone_contacts"]["Tim"]                  #del Tim from the dictionary
user_info["phone_contacts"]["Eve"] = "+4455526583" 
user_info["phone_contacts"]["Eve2"] = "+49563252765"    #add a new contact with 2 numbers (ez valószínűleg nem jó így)

#Extra 1
print(user_info["Skills"][-3:][::-1])                   #print the skills list last 3 items in a reverse order

#Extra 2
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2") #rename Tim2 to Tim

#Let's see the full dict now
for key, value in user_info.items():
    print(f"{key}: {value}")