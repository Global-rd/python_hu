import os
import logging

# Mappa- és fájlútvonal megadása
base_dir = 'homeworks/schreinerbalazs/4_exceptions_logging'
os.makedirs(base_dir, exist_ok=True)
file_path = os.path.join(base_dir, 'tasks.txt')

# Üres fájl létrehozása, ha nem létezik
if not os.path.exists(file_path):
    open(file_path, 'w').close()

# Logger beállítása
log_file_path = os.path.join(base_dir, 'task_manager.log')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler(log_file_path), logging.StreamHandler()])

def read_tasks():
    """Feladatok olvasása a fájlból."""
    try:
        with open(file_path, 'r') as file:
            tasks = file.readlines()
            logging.info("Feladatok sikeresen beolvasva.")
            return [task.strip() for task in tasks]
    except Exception as e:
        logging.error(f"Nem sikerült olvasni a feladatokat: {e}")
        return []

def add_task(task):
    """Új feladat hozzáadása a fájlhoz."""
    try:
        with open(file_path, 'a') as file:
            file.write(task + '\n')
            logging.info(f"Feladat hozzáadva: {task}")
    except Exception as e:
        logging.error(f"Nem sikerült hozzáadni a feladatot: {e}")

def remove_task(task):
    """Feladat törlése a fájlból."""
    try:
        tasks = read_tasks()
        if task in tasks:
            tasks.remove(task)
            with open(file_path, 'w') as file:
                for t in tasks:
                    file.write(t + '\n')
            logging.info(f"Feladat törölve: {task}")
        else:
            logging.warning(f"A feladat nem található: {task}")
    except Exception as e:
        logging.error(f"Nem sikerült törölni a feladatot: {e}")

def display_menu():
    """A felhasználói menü megjelenítése."""
    print("Válassz az alábbi opciók közül:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def main():
    """Felhasználói interakció kezelése a menü segítségével."""
    while True:
        display_menu()
        choice = input("Add meg a választásod (1-4): ")
        
        if choice == '1':
            task = input("Add meg a hozzáadandó feladatot: ")
            add_task(task)
        elif choice == '2':
            tasks = read_tasks()
            print("Feladatok:")
            for t in tasks:
                print(f"- {t}")
        elif choice == '3':
            task = input("Add meg a törlendő feladatot: ")
            remove_task(task)
        elif choice == '4':
            print("Kilépés...")
            break
        else:
            logging.warning("Érvénytelen választás. Kérlek válassz 1 és 4 között.")

if __name__ == "__main__":
    main()
