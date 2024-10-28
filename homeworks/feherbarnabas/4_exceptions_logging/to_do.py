import logging
import os

# Logging beállítás
File_Handler = logging.FileHandler("app.log")
File_Formatter = logging.Formatter('%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s')
File_Handler.setFormatter(File_Formatter)
File_Handler.setLevel(logging.DEBUG)

Stream_Handler = logging.StreamHandler()
Stream_Formatter = logging.Formatter('%(levelname)s - %(message)s - %(asctime)s')
Stream_Handler.setFormatter(Stream_Formatter)
Stream_Handler.setLevel(logging.ERROR)

logger = logging.getLogger()
logger.addHandler(File_Handler)
logger.addHandler(Stream_Handler)
logger.setLevel(logging.DEBUG)

file_path = "homeworks/feherbarnabas/4_exceptions_logging/tasks.txt"

# A fájl létrehozása
with open(file_path, "w") as file:
    file.write("")
    logger.info("File created.")

# Üres .txt fájl létrehozása
if not os.path.exists(file_path):
    open(file_path, 'w').close()

# Feladatok olvasása
def read_tasks():
    try:
        with open(file_path, 'r') as file:
            tasks = file.readlines()
            tasks = [task.strip() for task in tasks]
            logging.info(f"Tasks read: {tasks}")
            return tasks
    except Exception as e:
        logging.error(f"Error reading tasks: {e}")
        return []


# Feladat hozzáadása
def add_task(task):
    task = task.strip()
    if task:
        try:
            with open(file_path, 'a') as file:
                file.write(task + '\n')
            logging.info(f"Task added: {task}")
        except Exception as e:
            logging.error(f"Error adding task: {e}")
    else:
        print("I cannot add a blank to the list!")
        logging.warning("Tried to add a blank.")

# Feladat törlése
def remove_task(task):

    tasks = read_tasks()

    if not tasks:
        print("There are no tasks to remove.")
        return

    try:
        task_to_remove = input("Choose a task to remove: ")

        if task_to_remove in tasks:
            tasks.remove(task_to_remove)
            with open(file_path, 'w') as file:
                for t in tasks:
                    file.write(t + '\n')
            logging.info(f"Task removed: {task_to_remove}")
        else:
            logging.warning(f"Task not found: {task_to_remove}")
    except Exception as e:
        logging.error(f"Error removing task: {e}")

# Menü megjelenítése
def display_menu():
    print("\nTask manager:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

# Folyamatos input bekérés
def main():
    while True:
        display_menu()
        choice = input("Choose a number (1-4): ")
        if choice not in ['1', '2', '3', '4']:
            print("Invalid number, please choose between 1 and 4.")
            continue
        
        if choice == '1':
            task = input("Add a new task: ")
            add_task(task)
        elif choice == '2':
            tasks = read_tasks()
            if tasks:
                print("Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("There are no tasks.")
        elif choice == '3':
            tasks = read_tasks()
            if tasks:
                print("Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                remove_task(task)
            else:
                print("There are no tasks.")

        elif choice == '4':
            print("Exiting...")
            break
main()