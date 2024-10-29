import os
import logging

file_handler = logging.FileHandler("app.log")
stream_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

file_handler.setLevel(logging.DEBUG)
stream_handler.setLevel(logging.DEBUG)

logger = logging.getLogger()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

file_path = "homeworks/becseipeter/4_exceptions_logging/empty.txt"

def read_file_line_by_line(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line

def add_task(task):
    try:  
        with open(file_path, "a") as file:  
            logger.info(f"succesfully added task: {task}\n")
            file.close()
    except Exception as e:
        logger.error(f"Error adding task: {e}")
    
def view_all_tasks():
    try:
        with open(file_path, "r") as file:
            for line in file:
                print(line)
        logger.info("succesfully read file")
    except Exception as e:
        logger.error(f"Error reading tasks: {e}")


def remove_task(task):
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
        with open(file_path, "w") as f:
            for line in lines:
                if line.strip("\n") != task:
                    f.write(line)
    except Exception as e:
        logger.error(f"Error while deleting task: {e}")


def display_menu():
    
    menu_input = input("Please enter one of the following options:\n 1 - add task\n 2 - view all tasks\n 3 - remove task\n 4 - exit\n")

    if menu_input == "1":
        task = input("Please add task\n")
        add_task(task = task)
    elif menu_input == "2":
        view_all_tasks()
    elif menu_input == "3":
        task = input("Please remove task\n")
        remove_task(task = task)
      
    elif menu_input == "4":
        exit()

display_menu()