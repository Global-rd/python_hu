
name = input("Kérlek add meg a neved: ")
name = name.strip().capitalize()
age = input("Kérlek add meg az életkorod: ")
age = int(age)
agedays = age*365
xp = input("Kérlek add meg hány éves Python tapasztalatod van: ")

#-----szorgalmi
proxp = input("Szeretnéd, hogy a karaktered profi Python fejlesztő legyen? (yes or no) ")
proxp = True if proxp == "yes" else False
proxp = bool(proxp)

if proxp == True:
    print(f"My character is {agedays} days old. His name is {name} and he has {xp} years of Python experience. He wants to be a Python developer!")
if proxp == False:
    print(f"My character is {agedays} days old. His name is {name} and he has {xp} years of Python experience. He does not want to be a Python developer!")
#-----szorgalmi