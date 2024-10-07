# Adatok bekérése
name = input("Add meg a karakter nevét: ")
age_in_years = input("Add meg a karakter életkorát (évben): ")
python_experience = input("Add meg a Python tapasztalatot években: ")
wants_to_be_dev = input(
    "Szeretné, hogy a karakter profi Python fejlesztő legyen? (yes/no): ")

# Adattisztítás és típuskonverzió
name = name.strip().title()
age_in_years = int(age_in_years)
python_experience = int(python_experience)

# Ternary operator használata a válasz alapján
wanna_be_pro_dev = True if wants_to_be_dev.lower() == "yes" else False
# A tényleges szöveget adjuk meg a változónak, a fenti részt azért hagyom bent, mert booleant kért a feladat :)
wants_to_be_dev = "wants" if wanna_be_pro_dev else "does not want"

# Életkor kiszámítása napokban
# Feltételezzük, hogy ma van a születésnapja, nincs szökőév figyelembe véve
age_in_days = age_in_years * 365

# Kiírás
print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_experience} years of experience. "
      f"He/she {wants_to_be_dev} to be a Python developer!")
