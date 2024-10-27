"""Feladat 1: 
Hozz létre egy to_do.py nevű file-t, és kódold le a következő feladat megoldását:
- OK / Készíts egy Feladatkezelő alkalmazást! 
- OK / Hozz létre egy .txt file-t és hagyd üresen.
- OK / Definiálj 3 függvényt a következőkre: feladatok olvasása, egy feladat hozzáadása, egy feladat törlése.
- OK / Legyen egy display_menu() function-öd is, ami kiprinteli a lehetséges opciókat:
    * Add Task
    * View Tasks
    * Remove Task
    * Exit
- Folyamatosan kérj be inputot a felhasználótól hogy ezek közül a menüpontok közül mit szeretne csinálni, és hívd meg a válaszhoz megfelelő függvényt.
- A felhasználó inputja 1,2,3 vagy 4 kell, hogy legyen, ellenőrizd! Ha az 1-es vagy 3-as opciót választja, mindkét esetben paramétert kell átadnod a megfelelő függvénynek. “Exit”-re lépjen ki a program.
- Használj hibakezelést a file-ba való íráskor és olvasáskor, illetve használd a logging module-t. Egyszerre logolj a konzolra és egy .log file-ba. A .txt file legyen része a pull request-nek, de a log file-ok ne! Használd a .gitignore-t!

Extra: Alakítsd át a .txt file-os megoldást úgy, hogy egy json file-t használsz a feladatok trackelésére!
"""
import time as tm
import sys
import os
import logging

filepath = "homeworks/veizerattila/4_exceptions_logging/To_do.txt"

###############################################################################
### Logolási környezet definiálása ############################################
###############################################################################
file_handler = logging.FileHandler("homeworks/veizerattila/4_exceptions_logging/To_do_app.log")
stream_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

file_handler.setLevel(logging.INFO)
stream_handler.setLevel(logging.INFO)

logger = logging.getLogger()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)

###############################################################################
### Függvények definiálása ####################################################
###############################################################################
def view_task():
    try:
        with open(filepath, "r", encoding='utf-8-sig') as file:
            logging.info("Viewing tasks.")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        logging.error(f"The file '{filepath}' does not exist.")
        print(f"The file '{filepath}' does not exist. Please create it or check the path.")

def add_task (task):
    with open (filepath , "a") as file:
        file.write(f"{task}\n")
    logging.info(f"Task {task} added to the To-Do app. ")
    #print(f"{task} has been added to your To-Do app. ")
    view_task()

def remove_task (taskremove):
    while True:
        with open(filepath, "r") as file:
            #items = [i.strip() for i in file]
            items = list(set([i.strip() for i in file]))  # Duplikátumok eltávolítása
        if taskremove.strip() in items:
            confirm = input(f"Do you really want to delete the task {taskremove}? (Y or N)? ")    
            if confirm.capitalize() == "Y":
                items.remove(taskremove)
                logging.info(f"Task {taskremove} removed. ")
                #print(f"The following task has has been removed: {taskremove}")
                with open ( filepath, "w") as file:
                    file.writelines('\n'.join(items) + '\n')
                view_task()
            else:
                logging.info(f"Task {taskremove} not removed. ")
                #print(f"Task {taskremove} not removed.")
        else:
            logging.warning(f"No '{taskremove}' task in the list. ")
            #print(f"There is no '{taskremove}' task in the list. ")
        taskremove = input("Please enter another task to remove or press Enter to exit: ")
        if not taskremove:
            break
        
"""     start_over_delete = input("Do you want to choose another task to remove (Y or N) ")
        view_task()
        if start_over_delete.capitalize() != "Y":
            break
        taskremove = input("Please enter another task to remove: ")"""

###############################################################################
### Kezdőoldal definiálása ####################################################
###############################################################################

def display_menu():
    logging.info("Listing options:")
    #print("You have the following options with this To-Do list app:")
    print("1: Add Task")
    print("2: View Tasks")
    print("3: Remove Task")
    print("4: Exit")

###############################################################################
### Programtörzs definiálása ##################################################
###############################################################################    
while True:
    try:
        display_menu()
        option = int(input("Choose a task from the above list of options: "))
        logging.info(f'Option {option} choosen. ')
        
        if option == 1:
            new_task = input("What is the new task you want to add? ")
            add_task(new_task)
            
        elif option == 2:
            try:
                view_task()
            except FileNotFoundError as e:
                logging.error(e)
                print(e)
            
        elif option == 3:
            try:
                view_task() # a Törlésnél is a nézetnél definiált hibakeresést használom fel újra, hogy
                            # ha nem  létezik a fájl, akkor egyből írja ki a választható opciókat.
                task_to_remove = input("Which task do you want to remove? ")
                remove_task(task_to_remove)
            except FileNotFoundError as e:
                logging.error(e)
                print(e)
            
        elif option == 4:
            logging.info("Exiting the app")
            print("See you later! ")
            break

        else:
            logging.error("Wrong option, not in 1,2,3 or 4. ")
            print("Wrong option. Please try again, choosing from 1, 2, 3 or 4. ")
    
    except ValueError:
            logging.error("Wrong option, not a number. ")
            print("Wrong option. Please enter a number. ")

""" start_over = input(f"Do you want to start over and choose from the following options? (Y or N) ")
    if start_over.capitalize() != "Y":
        logging.info("Exiting the app")
        #print("See you later! ")
        break"""