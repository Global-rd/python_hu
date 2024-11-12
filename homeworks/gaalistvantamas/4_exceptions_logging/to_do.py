"""
Author: Gaál István Tamás
Task: Homework-4
"""
import logging

# log setup
LOG_FILE_PATH = "homeworks/gaalistvantamas/4_exceptions_logging/todo.log"

file_handler = logging.FileHandler(LOG_FILE_PATH)
stream_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

file_handler.setLevel(logging.INFO)
stream_handler.setLevel(logging.INFO)

logger = logging.getLogger()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)

# Task Manager

FILE_PATH = "homeworks/gaalistvantamas/4_exceptions_logging/todo.txt"

try:
    with open(FILE_PATH, "x") as file:
        file.write("")
except:
    print("The file is already exist.")

def display_menu():
    print("\n1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Exit\n")

def add_task(task: str):
    try:
        with open(FILE_PATH, "a") as file:
            file.write(f"{task}" + ",")

    except:
        print("Add task Fail!")

    logger.info(f"Task {task} is added!")

def view_task():
    try:
        with open(FILE_PATH, "r") as file:
            tasks = file.read()
            task_list = list(tasks.split(","))

            if (len(task_list) - 1):
                for task in task_list:
                    if not task == "":
                        print(f"{task.strip()}")
            else:
                print("The list is empty!")
            
    except:
        print("File is not exist or reading problems!")

def remove_task(removable_task: str):
    try:    
        with open(FILE_PATH, "r") as file:
            tasks = file.read()
            task_list = list(tasks.split(","))

            if removable_task in task_list:
                for task in task_list:
                    if task == removable_task:
                        task_list.remove(task)
                        logger.info(f"Task {removable_task} is removed!")
            
                with open(FILE_PATH, "w") as file:
                    for task in task_list:
                        if not task == "":
                            file.write(f"{task}" + ",")
            else:
                print("This task is not in list!")

    except:
        print("Remove task Fail!")

def choose_from_the_menu():
    while True:
        display_menu()
        choose = input("Choose from the menu:")
    
        if choose == '1':
            task = input("Add a new task!\n")
            add_task(task)
        elif choose == '2':
            view_task()
        elif choose == '3':
            view_task()
            removable_task = input("Please give a name of the task that you want to delete!\n")
            remove_task(removable_task)
        elif choose == '4':
            exit()
        else:
            continue

choose_from_the_menu()