# Adatok bekérése
city = input("Kérlek add meg a várost: ")
rent = float(input("Kérlek add meg az albérlet árát (USD): "))

# Feltételek
if city.lower() == "new york" or city.lower() == "san francisco":
    if rent < 4000:
        result = "Be tudok költözni"
    else:
        result = "Nem tudok beköltözni"
elif city.lower() == "washington":
    result = "Nem akarok itt lakni"
elif city.lower() == "chicago":
    result = "Itt szívesen laknék. Pénz nem számít!"
else:
    if rent <= 3000:
        result = "Be tudok költözni"
    else:
        result = "Nem tudok beköltözni"

# Eredmény
print(f"Város: {city}, Albérlet ára: {rent} USD. {result}")