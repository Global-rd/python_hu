# képzeletbeli karakterem

# inputok bekérése
name = input("Hogy hívnak?").strip().capitalize() # név bekérése nagybetűvel és szóközök nélkül
age = int(input("Hány éves vagy?").strip()) # kor bekérése és konvertálása egész számmá
python_exp_in_years = int(input("Hány éve foglalkozol phyton programozással?")) #Tapasztalatok években

# életkora napokban
age_in_days = age * 365

# extra feladat_1
you_want_to_be_python_dev = input("Szeretnél Python fejlesztő lenni? (yes/no):").strip().lower()

# ternary operátor: kicsit editáltam, hogy tisztább legyen a kód
python_dev_status = ("profi Python fejlesztő szeretne lenni"
if you_want_to_be_python_dev == "yes"
else "nem szeretne Python fejlesztő lenni")

# eredmény
print(f"""A karakterem neve {name}, {age_in_days} napos, és 
{python_exp_in_years} éve foglalkozik Python programozással. 
A karakterem {python_dev_status}.""")