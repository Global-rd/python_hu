"""Feladat 1: 
Hozz létre egy to_do.py nevű file-t, és kódold le a következő feladat megoldását:
Készíts egy Feladatkezelő alkalmazást! 
Hozz létre egy .txt file-t és hagyd üresen.
Definiálj 3 függvényt a következőkre: feladatok olvasása, egy feladat hozzáadása, egy feladat törlése.
Legyen egy display_menu() function-öd is, ami kiprinteli a lehetséges opciókat:
Add Task
View Tasks
Remove Task
Exit
Folyamatosan kérj be inputot a felhasználótól hogy ezek közül a menüpontok közül mit szeretne csinálni,
és hívd meg a válaszhoz megfelelő függvényt.
A felhasználó inputja 1,2,3 vagy 4 kell, hogy legyen, ellenőrizd! Ha az 1-es vagy 3-as opciót választja,
mindkét esetben paramétert kell átadnod a megfelelő függvénynek. “Exit”-re lépjen ki a program.
Használj hibakezelést a file-ba való íráskor és olvasáskor, illetve használd a logging module-t.
Egyszerre logolj a konzolra és egy .log file-ba. A .txt file legyen része a pull request-nek,
de a log file-ok ne! Használd a .gitignore-t!

Extra: Alakítsd át a .txt file-os megoldást úgy, hogy egy json file-t használsz a feladatok trackelésére!
"""
#egyéb szükséges dolgok
import os
import logging

#file elérési helye

base_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(base_dir, 'jonasnikolett.txt')
log_file = os.path.join(base_dir, 'to_do_log.log')

#loggolás meghatározása
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


#file megnyitása és hozzáírás meghatározása
def read_tasks(filename):
    try:
        with open(filename, 'r'):
            tasks = filename.readlines()
            logging.info("Registered task / Feladat beírásra került")
            return tasks
    except FileNotFoundError:
        logging.error("File not found! / A fájl nem található.")
        return []

def add_task(filename, task):
    try:
        with open(filename, 'a'):
            filename.write(task + '\n')
            logging.info(f"Task added: / Feladat hozzáadva: {task}")
    except IOError:
        logging.error("Somthing wrong! Hiba történt.")

def remove_task(filename, task_index):
    tasks = read_tasks(filename)
    if task_index >= 0 and task_index < len(tasks):
        removed_task = tasks.pop(task_index).strip()
        with open(filename, 'w') as f:
            for task in tasks:
                filename.write(task.strip() + '\n')
        logging.info(f"FTask deleted: /Feladat törölve: {removed_task}")
    else:
        logging.warning("This task not avaiable / A feladat nem létezik")

# feladatok meghatározása ami megjelenik a felhasználó számára
def display_menu():
    print("1. Add Task / Feladat hozzásadása")
    print("2. View Tasks /Feladatok megnézése")
    print("3. Remove Task / Feladat törlése")
    print("4. Exit / Kilépés a programból")
    


while True:
    display_menu()
    choice = input("Choose for the following menu / Válasszon egy menupontot: ")
    try:
        choice = int(choice)

        if choice == 1:
            logging.info("The user chose option 1 / A felhasználó az 1. opciót választotta")
            task = input("Enter the task / Adja meg a feladatot: ")
            add_task(data_file, task)
            print(f"Task added / A feladat hozzáadva {task}!")
            print("______________________________________________________")

        elif choice == 2:
            logging.info("The user chose option 2 /A felhasználó az 2. opciót választotta")
            tasks = read_tasks(data_file)
            if tasks:
                print("______________________________________________________")
                print("Task list / Feladatok listája:")
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task.strip()}")
                print("______________________________________________________")
            else:
                print("No task / Nincsenek feladatok.")
                logging.error("No avaiable task / Nincs listázható feladat")

        elif choice == 3:
            logging.info("The user chose option 3 / A felhasználó az 3. opciót választotta")
            tasks = read_tasks(data_file)
            if tasks:
                print("")
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task.strip()}")
                index = int(input("Which tasked should it delete? / Melyik feladatot töröljem? ")) - 1
                remove_task(data_file, index)
            else:
                print("There are no tasks to delete / Nincsenek törölhető feladatok.")
                logging.error("There are no tasks to delete/ Nincs törölhető feladat.")

        elif choice == 4:
            print("Exit! / Kilépés!")
            logging.info("The user exit / A felhasználó kilépett")
            break
        else:
            print("Invalid selection. Choose from the listed menu items. / Érvénytelen választás. Válasszon a felsorolt menu pontok közül")
            logging.info("The user entered an incorrect menu / A felhasználó nem megfelelő menüt adott meg.")
    except ValueError:
        print("Invalid selection. The number of the menu item must be entered / Érvénytelen választás. A menupont számát kell megadni.")

