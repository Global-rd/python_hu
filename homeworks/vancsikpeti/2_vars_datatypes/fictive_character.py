
import gender_guesser.detector as gender
gen = gender.Detector()

character = {
    "name" : input("What is your name? (your firstname) ").strip().capitalize(),
    "age": int(input("How old are you? (in years) ")),
    "python_experience_years": int(input("How many years of python experiences do you have? (in years) "))
}
age_in_days = character["age"]*365
pronoun = ""
possessive_pronoun = ""
if gen.get_gender(character["name"]) == "male": 
    pronoun = "he"
    possessive_pronoun = "His"
elif gen.get_gender(character["name"]) == "female" : 
    pronoun = "she"
    possessive_pronoun = "Her"
else: 
    pronoun = "he/she"
    possessive_pronoun = "His/her"


# print(f"My character is {age_in_days} old. {possessive_pronoun} name is {character["name"]} and {pronoun} has {character["python_experience_years"]} years experience.")
# print(f"My character is {age_in_days} old. {possessive_pronoun} name is {character["name"]} and {pronoun} has {character["python_experience_years"]} years experience.")

# Extra feladat (szorgalmi):
be_python_dev = input("Do you want to be a professional python developer? (yes/no)")
bool_python_dev = True if be_python_dev.lower() == "yes" else False
print_text = "wants" if bool_python_dev == True else "does not want"

print(f"My character is {age_in_days} old. {possessive_pronoun} name is {character["name"]} and {pronoun} has {character["python_experience_years"]} years experience. {pronoun.capitalize()} {print_text} to be a Python developer!")
