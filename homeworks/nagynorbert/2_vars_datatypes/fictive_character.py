# 2. homework - Nagy Norbert

#user_inputs
fict_name = input("Please type your character's name:").strip().capitalize()
fict_age_days = 365 * int(input("Please add how many years old is your character:"))
fict_experience = int(input("How many years experencie does your character have in Python programming?"))

#extra
answer = ("yes","no")
fict_pro = input("Would your character be a pro Python developer? (Yes/No)").strip().lower()
while fict_pro not in answer:
    print("Answer has to be Yes or No.")
    fict_pro = input("Would your character be a pro Python developer? (Yes/No)").strip().lower()
match fict_pro:
    case "yes":
        fict_pro_bool = True
    case "no":
        fict_pro_bool = False

fict_pro_print = "He/she wants to be a Python developer!" if fict_pro_bool else "He/she does not want to be a Python developer!"

#printout
print(f"My character is {fict_age_days} old. His/her name is {fict_name} and he/she has {fict_experience} years experience. {fict_pro_print}")


