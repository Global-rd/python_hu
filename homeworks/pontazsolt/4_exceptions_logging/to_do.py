import os
import logging

# Feladatfájl elérési útvonala
tasklist = "homeworks/pontazsolt/4_exceptions_logging/tasklists.txt"

# Logging konfiguráció
file_handler = logging.FileHandler("task_manager.log")
stream_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

file_handler.setLevel(logging.INFO)
stream_handler.setLevel(logging.DEBUG)

logger = logging.getLogger("TaskManagerLogger")
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

# Ellenőrizzük, hogy a tasklist könyvtár és fájl létezik-e
if not os.path.exists(tasklist):
    os.makedirs(os.path.dirname(tasklist), exist_ok=True)
    with open(tasklist, "w") as file:
        pass
    logger.info("File of Tasklist created.")

# Task hozzáadása
def add_task(task):
    with open(tasklist, "a") as file:
        file.write(f"{task}\n")
    logger.info(f"Task has been added: {task}")
    print(f"Task has been added: {task}")

# Task olvasása
def read_tasks():
    try:
        with open(tasklist, "r") as file:
            tasks = file.readlines()
        if tasks:
            logger.info("Succesfully got tasks.")
            print("Tasks:")
            for num, task in enumerate(tasks, 1):
                print(f"{num}. {task.strip()}")
        else:
            logger.info("There is no task.")
            print("There is no task")
    except Exception as e:
        logger.error(f"Something went wrong until task reading: {e}")

# Task törlése
def remove_task(task_number):
    try:
        with open(tasklist, "r") as file:
            tasks = file.readlines()
        
        if 0 < task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1).strip()
            with open(tasklist, "w") as file:
                file.writelines(tasks)
            logger.info(f"Task removed: {removed_task}")
            print(f"Task removed: {removed_task}")
        else:
            logger.warning(f"Incorrect task number: {task_number}")
            print("Incorrect task number.")
    except ValueError:
        logger.error("Incorrect value.")
        print("Incorrect value, please use numbers.")
    except Exception as e:
        logger.error(f"Something went wrong until task removing: {e}")

# Menü megjelenítése
def display_menu():
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

# Fő program logika
def main():
    while True:
        display_menu()
        choice = input("Give a number (1-4): ")
        
        if choice == '1':
            task = input("Give the task: ")
            add_task(task)
        elif choice == '2':
            read_tasks()
        elif choice == '3':
            try:
                task_number = int(input("Give the number of the task to remove: "))
                remove_task(task_number)
            except ValueError:
                logger.error("Incorrect number.")
                print("Incorrect number.")
        elif choice == '4':
            logger.info("Exiting.")
            print("Exiting...")
            break
        else:
            logger.warning(f"Incorrect option: {choice}")
            print("Incorrect option, please choose from numbers 1-4.")

main()