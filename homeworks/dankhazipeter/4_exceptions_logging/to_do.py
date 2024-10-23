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


def load_tasks():
    try:
        with open(tasks_file, 'r') as f:
            tasks = json.load(f)
        logging.info("Tasks successfully read from file.")
        return tasks
    except Exception as e:
        logging.error(f"Error reading tasks: {e}")
        return []


def save_tasks(tasks):
    try:
        with open(tasks_file, 'w') as f:
            json.dump(tasks, f, indent=4)
        logging.info("Tasks successfully saved to file.")
    except Exception as e:
        logging.error(f"Error saving tasks: {e}")


def add_task(tasks, task):
    try:
        if task in tasks:
            print(f"A feladat '{task}' már létezik.")
            logging.warning(f"Task '{task}' already exists.")
        else:
            tasks.append(task)
            logging.info(f"Task '{task}' added successfully.")
    except Exception as e:
        logging.error(f"Error adding task: {e}")


def remove_task(tasks, task):
    try:
        if task in tasks:
            tasks.remove(task)
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


tasks = load_tasks()

while True:
    display_menu()
    try:
        choice = input("Válassz egy lehetőséget (1-4): ")
        if choice not in ["1", "2", "3", "4"]:
            print("Érvénytelen választás, kérlek 1 és 4 közötti számot adj meg.")
            continue

        if choice == "1":
            task = input("Add meg a hozzáadandó feladatot: ")
            add_task(tasks, task)
        elif choice == "2":
            if tasks:
                print("\nJelenlegi feladatok:")
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")
            else:
                print("\nNincsenek feladatok.")
        elif choice == "3":
            task = input("Add meg a törlendő feladatot: ")
            remove_task(tasks, task)
        elif choice == "4":
            save_tasks(tasks)
            print("Viszlát! Ha legközelebb elindítod a programot, folytathatod a feladatok kezelését ott, ahol abbahagytad.")
            break
    except Exception as e:
        logging.error(f"Úváratlan hiba: {e}")
