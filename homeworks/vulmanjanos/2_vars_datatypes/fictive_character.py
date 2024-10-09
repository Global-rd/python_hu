character_first_name = input("Please give me your first name:")
character_family_name = input("Give me your family name too:")
character_full_name = character_first_name + character_family_name
character_age = input("How old are you?")
character_python_experience = input("How many years Phyton experience you have?")

character_first_name = character_first_name.strip().capitalize()
character_family_name = character_family_name.strip().capitalize()

age = int(character_age)*365

print(character_first_name)
print(character_family_name)
print(character_age)
print(character_python_experience)

fictive_character_info = f"My character is {character_age} old. His name is {character_first_name} {character_family_name} and he has {character_python_experience} years experience."
print(fictive_character_info) 

