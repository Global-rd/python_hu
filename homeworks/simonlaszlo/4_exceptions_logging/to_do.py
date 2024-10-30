import logging
#import os

TASKS_FILE = "homeworks/simonlaszlo/4_exceptions_logging/log.log"
LOG_FILE = "homeworks/simonlaszlo/4_exceptions_logging/to_do.txt"

def add_task(task):
    """
    Új feladatot ad hozzá a fájlhoz.
    """
    try:
        with open(TASKS_FILE, "a") as file:
            file.write(task + "\n")
        logging.info(f"Feladat hozzaadva: '{task}'")
    except FileNotFoundError:
        logging.info("Fajl nem talalhato.")
    except PermissionError:
        logging.info("Nincs a fájlhoz irasi jogosultsag!")
    except (IOError,OSError) as e:
        logging.info(f"Fajlkezelesi hiba: {e}")
    except Exception as e:
        logging.info(f"Egyeb hiba: {e}")
    
           

def view_tasks():
    """
    Megjeleníti a tárolt feladatokat a fájlból.
    """
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()

        #if tasks:
            print("\nFeladatok listája:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")
            print()  # Üres sor a menü és a lista közé
            logging.info("Feladatok megtekintese sikeres.")
        #else:
        #    logging.info("Nincs feladat a listaban.")
        #   display_menu()
    except FileNotFoundError:
        logging.info("Fajl nem talalhato.")
    except (IOError,OSError) as e:
        logging.info(f"Fajlkezelesi hiba: {e}")
    except Exception as e:
        logging.info(f"Egyeb hiba: {e}")



def display_menu():
    print("")
    print("1. Add task")
    print("2. List tasks")
    print("3. Remove task")
    print("4. Exit")

def remove_task(task_number):
    """
    Egy megadott sorszámú feladatot töröl a fájlból.
    """
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()

        if not tasks:
            logging.info("Nincs mit torolni.")
            return

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1).strip()

            with open(TASKS_FILE, "w") as file:
                for task in tasks:
                    file.write(task)
            
            logging.info(f"Feladat torolve: '{removed_task}'")
        else:
            logging.info(f"Ervenytelen torlesi sorszam: {task_number}")
    except FileNotFoundError:
        logging.info("Fajl nem talalhato.")
    except (IOError,OSError) as e:
        logging.info(f"Fajlkezelesi hiba: {e}")
    except PermissionError:
        logging.info("Nincs a fájlhoz irasi jogosultsag!")
    except Exception as e:
        logging.info(f"Egyeb hiba: {e}")


# Logger létrehozása

logger = logging.getLogger()
logger.setLevel(logging.INFO)
    
# Formátum beállítása
formatter_console = logging.Formatter('%(message)s - %(levelname)s')
formatter_file = logging.Formatter('%(asctime)s -  %(levelname)s - %(message)s')

# Képernyőre írás
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter_console)
logger.addHandler(console_handler)

# Fájlba írás
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter_file)
logger.addHandler(file_handler)

while True:
    display_menu()
    try:
        choice = input("Add meg a választásod: ")

        if choice=="1":
            task = input("Add meg az új feladatot: ")
            add_task(task)
        elif choice=="2":
            view_tasks()
        elif choice=="3":
            task_empty=view_tasks()
            
            try:
                if task_empty != 0:
                    task_number = int(input("Add meg a törölni kívánt feladat sorszámát: "))
                    remove_task(task_number)
            except ValueError:
                logging.info("Nem megfelelő értéket adtál meg.")
                
        elif choice=="4":
            logging.info("Kilepes a programbol.")
            print("Kilepes...")
            break
        else:
            raise ValueError() #"1-4-ig lehet valasztani!"
    except ValueError:
        logging.info("Nem megfelelo erteket adtal meg.")    



