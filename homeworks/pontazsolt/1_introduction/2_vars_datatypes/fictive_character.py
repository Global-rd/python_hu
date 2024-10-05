#Inputs#
full_name = (input("Full name: ")).strip().upper()           #printed#

age = int(input("Age: "))                        #corrected#

python_experience = input("Python experience in years: ")      #printed#

while True:
    want_to_be_professional = input("Do you wanna be professional at Python?: ").strip().lower()    #Ternarized#
    if want_to_be_professional in ["yes", "no"]:
        break
    else:
        print("I can agree only 'yes' or 'no' answer")


#Corrections#
age_in_days = age * 365   #printed#


#Ternary operator#
ambitious = True if want_to_be_professional == "yes" else False             


#Introduction/Result#
if ambitious:
    print(f"My character is {age_in_days} old. His/her name is {full_name} and he/she has {python_experience} years experience. He/she wants to be a Python developer!")
else:
    print(f"My character is {age_in_days} old. His/her name is {full_name} and he/she has {python_experience} years experience. He/she does not wants to be a Python developer!")
