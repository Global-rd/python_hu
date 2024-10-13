# Bekérjük a felhasználótól az adatokat
name_input = input("Kérlek add meg a neved: ")
age_input = input("Kérlek add meg az életkorodat: ")
python_exp_input = input("Kérlek add meg, hány éve tanulsz Pythont: ")
wants_to_be_developer_input = input("Szeretnél profi Python fejlesztő lenni? (yes/no): ")

# A név nagybetűsítése és a szóközök eltávolítása
name = name_input.strip().upper()

# Az életkor konvertálása egész számmá
age_years = int(age_input)

# Az életkor napokban, feltételezve, hogy ma van a születésnapja
age_in_days = age_years * 365

# Python tapasztalat években
python_exp_in_years = int(python_exp_input)

# Boolean változó a fejlesztői ambíciók alapján
wants_to_be_developer = wants_to_be_developer_input.strip().lower() == "yes"

# Az információk kiírása
developer_message = "He/she wants to be a Python developer!" if wants_to_be_developer else "He/she does not want to be a Python developer!"
print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_exp_in_years} years experience. {developer_message}")
