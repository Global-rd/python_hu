import json
import logging
import os

# Logging beállítása
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])

# Mappa és fájl elérési útvonala
TODO_DIR = '4_exceptions_logging'
TODO_FILE = os.path.join(TODO_DIR, 'tasks.json')

# Ellenőrizzük, hogy a mappa létezik-e, ha nem, létrehozzuk
if not os.path.exists(TODO_DIR):
    os.makedirs(TODO_DIR)

# Feladatok olvasása
def read_tasks():
    if not os.path.exists(TODO_FILE):
        logging.warning("A fájl nem található, új fájl létrehozva.")
        with open(TODO_FILE, 'w') as file:
            json.dump([], file)
    
    try:
        with open(TODO_FILE, 'r') as file:
            tasks = json.load(file)
            return tasks
    except Exception as e:
        logging.error("Hiba történt a fájl olvasása közben: %s", e)
        return []

# Feladat hozzáadása
def add_task(task):
    tasks = read_tasks()
    tasks.append(task)
    try:
        with open(TODO_FILE, 'w') as file:
            json.dump(tasks, file)
            logging.info("Feladat hozzáadva: %s", task)
    except Exception as e:
        logging.error("Hiba történt a fájl írása közben: %s", e)

# Feladat törlése
def remove_task(task_index):
    tasks = read_tasks()
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        try:
            with open(TODO_FILE, 'w') as file:
                json.dump(tasks, file)
                logging.info("Feladat törölve: %s", removed_task)
        except Exception as e:
            logging.error("Hiba történt a fájl írása közben: %s", e)
    else:
        logging.warning("A megadott index nem érvényes.")

# Menü megjelenítése
def display_menu():
    print("\\n--- Feladatkezelő ---")
    print("1. Feladat hozzáadása")
    print("2. Feladatok megtekintése")
    print("3. Feladat törlése")
    print("4. Kilépés")

# Fő program
def main():
    while True:
        display_menu()
        choice = input("Válassz egy opciót (1-4): ")
        if choice == '1':
            task = input("Add meg a feladatot: ")
            add_task(task)
        elif choice == '2':
            tasks = read_tasks()
            if tasks:
                print("Feladatok:")
                for idx, task in enumerate(tasks):
                    print(f"{idx}. {task}")
            else:
                print("Nincsenek feladatok.")
        elif choice == '3':
            task_index = int(input("Add meg a törlendő feladat számát: "))
            remove_task(task_index)
        elif choice == '4':
            logging.info("Kilépés a programból.")
            break
        else:
            print("Érvénytelen opció, kérlek válassz 1-4-ig.")

if __name__ == "__main__":
    main()
