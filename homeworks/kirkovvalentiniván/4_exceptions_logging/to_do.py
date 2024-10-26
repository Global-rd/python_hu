import logging
import json


def setup_logger(logger_name, log_file="python_hu/homeworks/kirkovvalentiniván/4_exceptions_logging/app.log",level=logging.INFO):
    logger = logging.getLogger(logger_name)                                         #Call getlogger function from logging module
    file_handler = logging.FileHandler(log_file)                                    #Where we write the log messages
    stream_handler = logging.StreamHandler()                                          #Where we write the log messages
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')      #The format of the messages
    file_handler.setFormatter(formatter)                                            #Assigg the formatter to the handler
    stream_handler.setFormatter(formatter)                                          #Assigg the formatter to the handler
     
    file_handler.setLevel(logging.DEBUG)                                            #Assign the level of the message to the handler
    stream_handler.setLevel(logging.DEBUG)                                          #Assign the level of the message to the handler
    
    logger.addHandler(file_handler)                                                 #Add handler to the logger
    logger.addHandler(stream_handler)                                               #Add handler to the logger
    logger.setLevel(level)                                                          #Add level to the logger
    return logger

logger = setup_logger("to_do_logger")

def read_task(file):
    try:
        with open(file, "r") as file:
            tasks = file.readlines()
        if tasks:
            print("Tasks: ")
            for task in tasks:
                print(f"-{task.strip()}")
        else:
            print("The file is empty")
        return tasks
    except Exception as e:
        logger.error(f"Something unexpexted happened: {e}")
        return []


def add_task(file,task):
    try:
        with open(file,"a") as file:
            file.write(task + "\n")
        logger.info(f"Task appended: {task}")
    except Exception as e:
        logger.error(f"Error while appending the task: {e}")

def remove_task(file,task):
    try:
        tasks = read_task(file)
        if task + "\n" in tasks:
            tasks.remove(task + "\n")
            with open(file,"w") as file:
                for task in tasks:
                    file.write(task)
            logger.info(f"Task removed: {task}")
        else:
            logger.warning(f"Task not found: {task}")
    except Exception as e:
        logger.error(f"Could not remove task: {e}")


def display_menu():
    print("\nTask manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


def main():
    file = "python_hu/homeworks/kirkovvalentiniván/4_exceptions_logging/to_do.txt"
    while True:
        display_menu()
        choice = int(input("Pick an option from 1 to 4: "))

        if choice == 1:
            task = input("Enter the task: ")
            add_task(file,task)
        elif choice == 2:
            read_task(file)
        elif choice == 3:
            task = input("Enter the task you would like to remove: ")
            remove_task(file,task)
        elif choice == 4:
            print("Exit")
            break
        else:
            print("Invalid choice, please select again.")

main()
