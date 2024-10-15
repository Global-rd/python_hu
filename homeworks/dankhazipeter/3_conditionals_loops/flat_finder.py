"""
Ez a modul Sarah lakáskeresési problémáját oldja meg.

A program bekéri a felhasználótól egy város nevét és a havi lakbér összegét,
majd meghatározza, hogy Sarah beköltözhet-e az adott városba a megadott lakbérért,
figyelembe véve Sarah preferenciáit és pénzügyi korlátait.
"""


def can_sarah_move(city_name, rent_amount):
    """
    Meghatározza, hogy Sarah beköltözhet-e egy adott városba az adott lakbérért.

    Args:
    city_name (str): A város neve.
    rent_amount (float): A havi lakbér összege USD-ben.

    Returns:
    bool: True, ha Sarah beköltözhet, False, ha nem.
    """
    if city_name.lower() == "chicago":
        return True
    elif city_name.lower() == "washington":
        return False
    elif city_name.lower() in ["new york", "san francisco"] and rent_amount < 4000:
        return True
    elif rent_amount <= 3000:
        return True
    else:
        return False


# Felhasználói input bekérése
city = input("Kérem, adja meg a város nevét: ")
rent = float(input("Kérem, adja meg a havi lakbér összegét (USD): "))

# Eredmény kiszámítása és kiírása
result = can_sarah_move(city, rent)

print(f"Sarah {'be tud költözni' if result else 'nem tud beköltözni'} "
      f"{city} városba {rent} USD havi lakbérért.")
