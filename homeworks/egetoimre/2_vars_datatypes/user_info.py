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

#A 4 programozási nyelv bekérése, majd listába töltése
programming_lang = input("Adjon meg 4 programozási nyelvet, vesszővel elválasztva, szóközök nélkül: ").split(",")
user_info["skills"] = programming_lang

# ABC szerint rendezzük a favourite_meals elemeit
user_info["favourite_meals"].sort()

#favourite_meals utolsó előtti eleme
print(user_info["favourite_meals"][-2])

# "spaghetti" hozzáadása a favourite_meals listához
user_info["favourite_meals"].append("spaghetti")

#a 3. és 4. elem hozzáadása újra
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

#duplikátumok törlése
user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))

#utolsó és az első elem felcserélése
memoria = user_info["favourite_meals"][0]
user_info["favourite_meals"][0] = user_info["favourite_meals"][-1]
user_info["favourite_meals"][-1] = memoria

# új elem hozzáadaása a phone_contacts-hoz
user_info["phone_contacts"]["Imre"] = "+36307654321"

# Tim törlése
del user_info["phone_contacts"]["Tim"]

# új ember, 2 telefonszám
user_info["phone_contacts"]["Hilda"] = ["+36301234567", "+3619876543"]


print(user_info)