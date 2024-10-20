import logging
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(base_dir, 'egetoimre.txt')
log_file = os.path.join(base_dir, 'app.log')

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

def read_tasks(filename):
    try:
        with open(filename, 'r') as f:
            tasks = f.readlines()
            logging.info("Listázásra kerültek a feladatok")
            return tasks
    except FileNotFoundError:
        logging.error("A fájl nem található.")
        return []

def add_task(filename, task):
    try:
        with open(filename, 'a') as f:
            f.write(task + '\n')
            logging.info(f"Feladat hozzáadva: {task}")
    except IOError:
        logging.error("Hiba történt a fájlba íráskor.")

def remove_task(filename, task_index):
    tasks = read_tasks(filename)
    if task_index >= 0 and task_index < len(tasks):
        removed_task = tasks.pop(task_index).strip()
        with open(filename, 'w') as f:
            for task in tasks:
                f.write(task.strip() + '\n')
        logging.info(f"Feladat törölve: {removed_task}")
    else:
        logging.warning("A feladat nem található")

def display_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    display_menu()
    choice = input("Válasszon egy opciót: ")
    try:
        choice = int(choice)

        if choice == 1:
            logging.info("A felhasználó az 1. opciót választotta")
            task = input("Adja meg a feladatot: ")
            add_task(data_file, task)
            print(f"A {task} feladat hozzáadva!")
            print("")

        elif choice == 2:
            logging.info("A felhasználó az 2. opciót választotta")
            tasks = read_tasks(data_file)
            if tasks:
                print("---+++---+++---")
                print("Feladatok listája:")
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task.strip()}")
                print("---+++---+++---")
                print("")
            else:
                print("Nincsenek feladatok.")
                logging.error("Nincs listázható feladat")

        elif choice == 3:
            logging.info("A felhasználó az 3. opciót választotta")
            tasks = read_tasks(data_file)
            if tasks:
                print("")
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task.strip()}")
                index = int(input("Melyik feladatot töröljem? ")) - 1
                remove_task(data_file, index)
            else:
                print("Nincsenek törölhető feladatok.")
                logging.error("Nincs törölhető feladat.")

        elif choice == 4:
            print("Kilépés!")
            logging.info("A felhasználó kilépett")
            break
        else:
            print("Érvénytelen választás. 1-4-ig kell választani")
            logging.info("A felhasználó nem érvényes menü indexet adott meg.")
    except ValueError:
        print("Érvénytelen bemenet. A feladat indexét kell megadni.")
