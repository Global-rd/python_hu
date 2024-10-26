# Homework - Nagy Norbert
import setup_logger
import sys

taskfile="homeworks/nagynorbert/4_exceptions_logging/tasks.txt"
logger = setup_logger.setup_logger("root_logger")

def add_task(task):
    """Add one task to taskfile."""
    logger.info(f"Following task will be added to taskfile: {task}")
    try:    
        with open(taskfile,"a") as file:
            file.write(task+"\n")
    except FileNotFoundError as e:
        logger.info(f"File not found: {e}")
    except Exception as e:
        logger.info(f"Unexpected error happened during adding a task to file: {e}")
    else:
        logger.info(f"Add {task} task to {taskfile} was success.")

def view_tasks():
    try:
        with open(taskfile,"r") as file:
            lines = file.readlines()
    except FileNotFoundError as e:
        logger.info(f"File not found: {e}")
    except Exception as e:
        logger.info(f"Unexpected error happened during viewing taskfile: {e}")
    else:
        if len(lines) == 0:
            logger.info("Task file is empty")
        else:
            logger.info(f"{taskfile} content is:")
            for line in lines:
                print(line.strip())

def remove_task(task):
    """Remove one task from taskfile."""
    logger.info(f"Following task will be removed: {task}")
    try:
        with open(taskfile,"r") as file:
            lines = file.readlines()
        logger.info(f"Tasks before remove operation:")
        view_tasks()
    except Exception as e:
        logger.info(f"Exception happened during {taskfile} reading: {e}")
    else:
            with open(taskfile,"w") as file:
                try:
                    file.seek(0)
                    index = lines.index(task+"\n")
                except IndexError as e:
                    logger.info(f"Task is not found in file: {e}")
                except ValueError as e:
                    logger.info(f"Task is not defined in file: {e}")
                except Exception as e:
                    logger.info(f"Unexpected error happened during removing a task: {e}")
                else:
                    lines.pop(index)
                    logger.info("Task removal was success.")
                    logger.info(f"Tasks after remove operation:")
                    view_tasks()
                finally:
                    file.truncate()
                    file.writelines(lines)


def exit_program():
    logger.info("Program exited. Bye!")
    sys.exit()

def display_menu():
    print(" ---- This program handles tasks. ---- ")
    print("Here is the menu:")
    print("    1. Add task")
    print("    2. View tasks")
    print("    3. Remove task")
    print("    4. Exit")

def user_input():
    while True:
        try:
            user_input=int(input("Please add one menu item between 1 and 4: "))
        except ValueError as e:
            logger.info(f"Input is not integer: {e}")
        except Exception as e:
            logger.info(f"Unxpected event happened during user input: {e}")
        else:
            if user_input < 1 or user_input > 4:
                logger.info("Incorrect. Input has to be between 1 and 4!")
            else:
                logger.info("Valid input.")
                break
    return user_input

display_menu()
menu_item = user_input()
match menu_item:
    case 1:
        try:
            task=input(f"Please add the task which will be added to {taskfile} file:")
        except Exception as e:
            logger.info(f"Exception happened during task definition in case of adding a task: {e}")
        else:
            add_task(task)
    case 2:
        view_tasks()
    case 3:
        try:
            task=input(f"Please add the task which will be removed from {taskfile} file:")
        except Exception as e:
            logger.info(f"Exception happened during task definition in case of remove a task: {e}")
        else:
            remove_task(task)
    case 4:
        exit_program()

