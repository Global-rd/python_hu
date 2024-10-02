# 2. homework - Nagy Norbert
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

# 1.
input_skills = input("Please add 4 skills with comma separated format:")
user_info.update({"skills":input_skills.split(",")})
pprint(user_info)

# 2.
user_info["favourite_meals"].sort()

# 3.
pprint(user_info["favourite_meals"][-2])

# 4.
user_info["favourite_meals"].append("spaghetti")
pprint(user_info)

# 5.
user_info["favourite_meals"].extend(user_info["favourite_meals"][2:4])
pprint(user_info)

# 6.
fav_meals_l = user_info["favourite_meals"]
fav_meals_no_dupl_l = list(set(fav_meals_l))
fav_meals_no_dupl_l.sort()
user_info["favourite_meals"] = fav_meals_no_dupl_l
pprint(user_info)

# 7.
user_info["favourite_meals"][0] = "rantott_hus"
user_info["favourite_meals"][-1] = "somloi"
pprint(user_info)

# 8.
user_info["phone_contacts"].update({"Carter":"+321234"})
pprint(user_info)

# 9.
user_info["phone_contacts"].pop("Tim")
pprint(user_info)

# 10.
user_info["phone_contacts"].update({"Elisa":["+21345","+1234"]})
pprint(user_info)

# extras
print("Extras: -------------------")
pprint(user_info)
print(user_info["skills"][::-1])

phone_cont_dict = dict(user_info["phone_contacts"])
tim2_tel = phone_cont_dict.get("Tim2")
user_info["phone_contacts"].update({"Tim":tim2_tel})
user_info["phone_contacts"].pop("Tim2")
pprint(user_info)

