# Adatbekérés
name = input("Enter your name :  ").strip().capitalize()
age_in_days = int(input("Enter your age (year): ").strip())
python_exp_in_years = float(input("Enter your python experience (year): ").strip())

# Éb átszámolás napokra , szökőévet nem vesszük figyelembe
age_in_days = age_in_days * 365  

# Kiírás
print(f"My character is {age_in_days} days old. His/her name is {name} and he/she has {python_exp_in_years} years of experience.")