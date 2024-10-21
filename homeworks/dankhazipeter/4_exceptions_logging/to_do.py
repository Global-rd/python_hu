import os
import json
import logging

# Logging setup
# Ha nem itt hozom létre, akkor a gyökér könyvtárban jön létre, de az közös hely. Normál projektben nem ide tenném, de a házinak ez a mappája.
log_dir = "homeworks/dankhazipeter/4_exceptions_logging"
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(os.path.join(
                            log_dir, "task_manager.log")),
                        logging.StreamHandler()
                    ])

tasks_file = os.path.join(log_dir, "tasks.json")

# tasks.json létrehozása, ahogy a feladat kéri. Azonban ha már létezik, ne próbáljuk meg újra létrehozni, hanem használjuk a benne lévő feladatokkal együtt.
if not os.path.exists(tasks_file):
    with open(tasks_file, 'w') as f:
        json.dump([], f)


def read_tasks():
    try:
        with open(tasks_file, 'r') as f:
            tasks = json.load(f)
        logging.info("Tasks successfully read from file.")
        return tasks
    except Exception as e:
        logging.error(f"Error reading tasks: {e}")
        return []


def add_task(task):
    try:
        tasks = read_tasks()
        tasks.append(task)
        with open(tasks_file, 'w') as f:
            json.dump(tasks, f, indent=4)
        logging.info(f"Task '{task}' added successfully.")
    except Exception as e:
        logging.error(f"Error adding task: {e}")


def remove_task(task):
    try:
        tasks = read_tasks()
        if task in tasks:
            tasks.remove(task)
            with open(tasks_file, 'w') as f:
                json.dump(tasks, f, indent=4)
            logging.info(f"Task '{task}' removed successfully.")
        else:
            logging.warning(f"Task '{task}' not found.")
    except Exception as e:
        logging.error(f"Error removing task: {e}")


def display_menu():
    print("""
    Teendők listája Menü:
    1. Feladat hozzáadása
    2. Feladatok megtekintése
    3. Feladat törlése
    4. Kilépés
    """)


while True:
    display_menu()
    try:
        choice = input("Válassz egy lehetőséget (1-4): ")
        if choice not in ["1", "2", "3", "4"]:
            print("Érvénytelen választás, kérlek 1 és 4 közötti számot adj meg.")
            continue

        if choice == "1":
            task = input("Add meg a hozzáadandó feladatot: ")
            add_task(task)
        elif choice == "2":
            tasks = read_tasks()
            if tasks:
                print("\nJelenlegi feladatok:")
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")
            else:
                print("\nNincsenek feladatok.")
        elif choice == "3":
            task = input("Add meg a törlendő feladatot: ")
            remove_task(task)
        elif choice == "4":
            print("Viszlát! Ha legközelebb elindítod a programot, folytathatod a feladatok kezelését ott, ahol abbahagytad.")
            break
    except Exception as e:
        logging.error(f"Váratlan hiba: {e}")
