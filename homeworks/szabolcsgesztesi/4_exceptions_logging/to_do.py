import logging
import os

#Fájl neve és helye, ahol a feladatokat tároljuk
task_file = "homeworks/szabolcsgesztesi/4_exceptions_logging/Tasks.txt"

#Logfájl neve és helye, ahol a logokat tároljuk
log_file_path = "homeworks/szabolcsgesztesi/4_exceptions_logging/Task_Manager_logs.log"

# Menü megjelenítése
def display_menu():
    print("\nFeladatkezelő Alkalmazás")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

# Feladatok olvasása fájlból
def read_tasks():
    try:
        with open(task_file, 'r') as file:
            tasks = file.readlines()
            tasks = [task.strip() for task in tasks]  # Újsor karakterek eltávolítása
        logging.info("Feladatok sikeresen beolvasva.")
        return tasks
    except FileNotFoundError:
        logging.error("A fájl nem található.")
        return []
    except Exception as e:
        logging.error(f"Hiba történt a feladatok beolvasásakor: {e}")
        return []

# Új feladat hozzáadása a fájlhoz
def add_task(task):
    try:
        with open(task_file, 'a') as file:
            file.write(task + '\n')
        logging.info(f"Feladat hozzáadva: {task}")
    except Exception as e:
        logging.error(f"Hiba történt a feladat hozzáadásakor: {e}")


# Feladat törlése fájlból
def remove_task(task_index):
    tasks = read_tasks()
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        try:
            with open(task_file, 'w') as file:
                file.writelines([task + '\n' for task in tasks])
            logging.info(f"Feladat törölve: {removed_task}")
        except Exception as e:
            logging.error(f"Hiba történt a feladat törlésekor: {e}")
    else:
        logging.error("Érvénytelen feladat index.")

# A program fő része függvénnyel
def main():
    while True:
        display_menu()
        choice = input("Válassz egy lehetőséget (1-4): ")
        
        if choice == "1":
            task = input("Add meg a feladatot: ")
            add_task(task)
        elif choice == "2":
            tasks = read_tasks()
            if tasks:
                print("\nFeladataid:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
            else:
                print("Nincsenek feladatok.")
        elif choice == "3":
            tasks = read_tasks()
            if tasks:
                print("\nFeladataid:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                try:
                    task_index = int(input("Add meg a törlendő feladat számát: ")) - 1
                    remove_task(task_index)
                except ValueError:
                    logging.error("Kérlek, egy számot adj meg.")
            else:
                print("Nincsenek feladatok.")
        elif choice == "4":
            print("Kilépés...")
            break
        else:
            logging.error("Érvénytelen választás, kérlek, 1-4 között válassz.")

# Logolás
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler(log_file_path), logging.StreamHandler()])

# Program indítása
main()