import os
import logging
import json

file_handler = logging.FileHandler("python_hu/homeworks/vancsikpeti/4_exceptions_logging/todo.log")
fformatter = logging.Formatter('%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s')
file_handler.setFormatter(fformatter)
file_handler.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
sformatter = logging.Formatter('%(levelname)s - %(message)s - %(asctime)s')
stream_handler.setFormatter(sformatter)
stream_handler.setLevel(logging.ERROR)

logger = logging.getLogger()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

json_file_path = "python_hu/homeworks/vancsikpeti/4_exceptions_logging/to-do-list.json"

tasks = {"tasks": []}
#tasks= {"tasks": ["First task", "Second task", "Third task"]}

with open(json_file_path, "w") as file:
    json.dump(tasks, file)
    logger.info("Create file.")

def read_tasks(json_file_path) -> dict:
    try:
        with open(json_file_path, "r") as file:
            data = json.load(file)
        logger.info("Open file in reading mode. Load items in file to list.")
    except Exception as error:
        logging.error("Valami hiba")    
    return data    

def view_task(json_file_path, key_word = "tasks"):
    data = read_tasks(json_file_path)
    tasks = data["tasks"]
    task_num = 1
    try:
        for task in tasks:
            print(f"{task_num}. task: {task.strip()}")
            task_num += 1
        print("---- end of the list ----")
    except TypeError as error:
        logger.error("NoneType object is not iterable")
    logger.info("Read the items from file.") 

def add_task(newtask):
    try:
        data = read_tasks(json_file_path)
        data["tasks"].append(newtask)
        with open(json_file_path, "w") as file:
            json.dump(data, file)
    except TypeError as error:
        logger.error("Error message... This part of the json object not a list.")    
    logger.info(f"Create a new task: {newtask}.")

def remove_task(task_item):
        tasks = []
        if task_item > 0:
            data = read_tasks(json_file_path)
            tasks = data["tasks"]
            del tasks[task_item-1]
            logger.info("Delete item from list.")
            new_object = {"tasks": tasks}
            #print(f"Törlés után az új lista elemei: {tasks}")
            with open(json_file_path, "w") as file:
                json.dump(new_object, file)
            print("Remove complete...\n")
        else:
            # print("Error message... This item is less than the number of your tasks. \n")
            logger.error(f"The received item is less than the number of your tasks. {task_item}")

def display_menu():
    print("1. Add Task || 2. View Tasks || 3. Remove Task || 4. Exit \n ----")
    logger.info("Show the display menu.")

def navigation():
    job = 0
    while True:  
        try: 
            job = int(input("Program navigation: "))
            logger.info(f"Input data for programm navigation: {job}")
        except ValueError as error:
            logger.error(f"Wrong data to input. {job}")
            return False
        if job < 1 or job > 4:
            logger.error(f"Wrong data to input. {job}")
            return False        
        return job

# main
while True:
    display_menu()
    logger.info("Show display menu.")
    job = navigation()
    logger.info("End navigation method.")
    if job == 1:
        task = input("Write your task what you want to do: ")
        logger.info(f"Enter task item. {task}")
        add_task(task)
    elif job == 2:
        view_task(json_file_path, "tasks")
    elif job == 3:
        try: 
            remove_item = int(input("Write the number of list's item that you want to remove: "))
            remove_task(remove_item)
        except ValueError as error:
            logger.error("Error message... It is not a number!")
        except IndexError as error:
            logger.error("Error message... This item is greater than the number of your tasks.")
    elif job == 4:
        logger.info("User exits.")
        print("Exit")
        break

"""
Feladat 1:

Hozz létre egy to_do.py nevű file-t, és kódold le a következő feladat megoldását:
Készíts egy Feladatkezelő alkalmazást! 
Hozz létre egy .txt file-t és hagyd üresen.
Definiálj 3 függvényt a következőkre: feladatok olvasása, egy feladat hozzáadása, egy feladat törlése.
Legyen egy display_menu() function-öd is, ami kiprinteli a lehetséges opciókat:
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Folyamatosan kérj be inputot a felhasználótól hogy ezek közül a menüpontok közül mit szeretne csinálni, és hívd meg a válaszhoz megfelelő függvényt.
A felhasználó inputja 1,2,3 vagy 4 kell, hogy legyen, ellenőrizd! 
Ha az 1-es vagy 3-as opciót választja, mindkét esetben paramétert kell átadnod a megfelelő függvénynek. “Exit”-re lépjen ki a program.
Használj hibakezelést a file-ba való íráskor és olvasáskor, illetve használd a logging module-t. Egyszerre logolj a konzolra és egy .log file-ba. 
A .txt file legyen része a pull request-nek, de a log file-ok ne! Használd a .gitignore-t!

Extra: Alakítsd át a .txt file-os megoldást úgy, hogy egy json file-t használsz a feladatok trackelésére!

"""