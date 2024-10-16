def can_move(city, rent):
    # Feltételek
    if city in ["new york", "san francisco"]:  # Membership operator használata
        if rent < 4000:
            return "Be tudok költözni"
        else:
            return "Nem tudok beköltözni"
    elif city == "washington":
        return "Nem akarok itt lakni"
    elif city == "chicago":
        return "Itt szívesen laknék. Pénz nem számít!"
    else:  # Egyesített else ág
        if rent <= 3000:
            return "Be tudok költözni"
        else:
            return "Nem tudok beköltözni"

def main():
    # Adatok bekérése
    city = input("Kérlek add meg a várost: ").lower()  # Kisbetűs város név
    try:
        rent = float(input("Kérlek add meg az albérlet árát (USD): "))  # Hibakezelés az albérlet áránál
        result = can_move(city, rent)  # Funkció hívása
        # Eredmény
        print(f"Város: {city.capitalize()}, Albérlet ára: {rent} USD. {result}")
    except ValueError:
        print("Kérlek, érvényes számot adj meg az albérlet áránál!")

if __name__ == "__main__":
    main()  # Fő program indítása
