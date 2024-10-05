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

#1.ask four progrmming language, convert to string add to existing dictionary as "skills"
skill = input("Write four programming languages separated by a comma, no spacing!: ").split(",") #converting to list at the same time
user_info["skills"]=skill #adding to the dictionery named skills (could have been solved with a chain method)

#2.print favourite_meals list elements in ascending per ABC
user_info["favourite_meals"].sort()

#3.print last item of favourite_meals
print()
print("------------------------")
print()
print(f"My favourite meal is {user_info['favourite_meals'][-2]}")
print()
print("------------------------")
print()
pprint(user_info) #full data printed as requested in tipp

#4. adding a "spaghetti" string to the list
user_info["favourite_meals"].append("spaghetti")

#5. create a new favourite_meals list by adding from current favourite_meals list 3. and 4. item
user_info["favourite_meals"].extend([user_info["favourite_meals"][2], user_info["favourite_meals"][3]])

#6. delete duplicates from favourite_meals
user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))

#7. change the first and the last item of the favourite-meals list
user_info["favourite_meals"][0], user_info["favourite_meals"][-1]=user_info["favourite_meals"][-1], user_info["favourite_meals"][0]

#8. add a new user to the phone_contacts
user_info["phone_contacts"]["Csenge"]= "+36301234567"

#9. delete Tim and his phone number from phone_conatcts
del user_info["phone_contacts"]["Tim"]

#10. add a user with 2 phone number
user_info["phone_contacts"]["Carol"]="+362022222222","+363033333333"

print()
print("------------------------")
print()
print("Summary:") #printed a summary of the homework 2
print()
pprint(user_info)
print()
print("------------------------")
print()
print("Extra Task 1")
#Print the skills list last 3 items reverse
reversed_skills = user_info["skills"][-1:-4:-1]
print(reversed_skills)
reversed_skills = user_info["skills"] #restore skills
print()
print("Extra Task 2")
#Extra 2: rename Tim2 to Tim
user_info["phone_contacts"]["Tim"] = user_info["phone_contacts"].pop("Tim2")
print()
pprint(user_info)