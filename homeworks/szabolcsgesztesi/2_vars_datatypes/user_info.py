# Táblázat amivel indulunk

user_info = {
    "name": "Mike",
    "age": 25,
    "favourite_meals": ["pizza","carbonara","sushi"],
    "phone_contacts": {
        "Mary": "+36701234567",
        "Tim": "+36207654321",
        "Tim2": "+36304567321",
        "Jim": "+364005000"
    }
}

# 1. feladat: 
proglang = input("Adj meg 4 programozási nyelvet vesszővel elválasztva!"  )
proglang = proglang.split(",")
user_info["skills"] = proglang

# 2. feladat: 
user_info["favourite_meals"].sort()

# 3. feladat: 
print(user_info["favourite_meals"][2])

# 4. feladat: 
user_info["favourite_meals"].append("spaghetti")

# 5. feladat: i
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])

# 6. feladat: (sajnos a set randomizálja, az abc-sorrend elveszik)
user_info["favourite_meals"] = list(dict.fromkeys(user_info["favourite_meals"]))

# 7. feladat:
user_info["favourite_meals"][0],user_info["favourite_meals"][-1] = user_info["favourite_meals"][-1],user_info["favourite_meals"][0]

# 8. feladat:
user_info["phone_contacts"]["Bob"] = "+36301234567"

# 9. feladat:
user_info["phone_contacts"].pop("Tim")

# 10. feladat:
user_info["phone_contacts"]["Frank"] = ["+36301234567","+36701112288"]

print(user_info)