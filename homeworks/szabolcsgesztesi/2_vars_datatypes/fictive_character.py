
name = input("Kérlek add meg a neved: ").strip().capitalize()
age = input("Kérlek add meg az életkorod: ")
age = int(age)
agedays = age*365
python_exp_in_years = input("Kérlek add meg hány éves Python tapasztalatod van: ")

#-----szorgalmi
proxp = input("Szeretnéd, hogy a karaktered profi Python fejlesztő legyen? (yes or no) ")
proxp = "wants" if proxp == "yes" else "does not want"
print(f"My character is {agedays} days old. His name is {name} and he has {python_exp_in_years} years of Python experience. He {proxp} to be a Python developer!")
#-----szorgalmi