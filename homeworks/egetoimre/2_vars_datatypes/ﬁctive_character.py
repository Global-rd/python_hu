# Adatok bekérése
name = input("Adja meg a nevét: ").strip().title()
age = int(input("Adja meg az életkorát években: "))
python = int(input("Hány éve foglalkozik Python-nal? "))

# Az életkor napokban. Szökőév figyelembevétele nélkül
# Szerintem a 365.25-tel való szorzás nem pontos eredményt ad, ha kerekítjük. Csak "for" ciklussal lehet megállapítani pontosan a napok számát, de azt még nem tanultuk :)
age_in_days = age * 365

#Házi első része:
print(f"My character is {age_in_days} old. His/her name is {name} and he/she has {python} years experience.")

# Profi Python fejlesztő szeretne lenni?
python_pro = input("Szeretne profi Python fejlesztő lenni? (igen/nem): ").strip().lower()
answer = True if python_pro == "igen" else False

# Házi extra feladat:
print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python} years experience. He/she {"wants" if answer else "does not want"} to be a Python developer!")
