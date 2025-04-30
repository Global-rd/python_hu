import os
import time

# Képernyő törlése
def clear_screen():
    if os.name == 'nt':  # Windows esetén
        os.system('cls')
    else:  # Linux/Mac esetén
        os.system('clear')

# Függvények a menü pontokhoz
def option_1():
    print("1. menüpont: Függvény 1 fut...")
    time.sleep(2)  # Alvás 2 másodpercig, hogy látható legyen a kimenet

def option_2():
    
    print("2. menüpont: Függvény 2 fut...")
    time.sleep(2)

def option_3():
    print("3. menüpont: Függvény 3 fut...")
    time.sleep(2)

def menu():
    while True:
        clear_screen()
        print("Válassz egy menüpontot:")
        print("1. Menüpont 1")
        print("2. Menüpont 2")
        print("3. Menüpont 3")
        print("0. Kilépés")

        choice = input("Választás: ")

        if choice == '1':
            option_1()
        elif choice == '2':
            option_2()
        elif choice == '3':
            option_3()
        elif choice == '0':
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás!")
            time.sleep(2)

# Menü indítása
menu()
