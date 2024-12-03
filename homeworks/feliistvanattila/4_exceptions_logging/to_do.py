import logging

# Logging beállítása
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        # logging.FileHandler ("homeworks/feliistvanattila/4_exceptions_logging/task_manager.log"),
                        logging.FileHandler("task_manager.log"),
                        logging.StreamHandler()
                    ])

# Fájl neve, ahol a feladatokat tároljuk
# TASK_FILE = "homeworks/feliistvanattila/4_exceptions_logging/tasks.txt"
TASK_FILE = "tasks.txt"


def read_tasks() -> list:
    try:
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()
            tasks = [task.strip() for task in tasks]
        logging.info("Tasks read successfully.")
        return tasks
    except FileNotFoundError:
        logging.error("The task file was not found.")
        return []


def add_task(task: str):
    try:
        with open(TASK_FILE, "a") as file:
            file.write(task + "\n")
        logging.info(f"Task '{task}' added successfully.")
    except Exception as e:
        logging.error("An error occurred while adding the task.")
        logging.exception(e)

# Feladat törlése a fájlból


def remove_task(task: str):
    tasks = read_tasks()
    if task in tasks:
        tasks.remove(task)
        try:
            with open(TASK_FILE, "w") as file:
                for t in tasks:
                    file.write(t + "\n")
            logging.info(f"Task '{task}' removed successfully.")
        except Exception as e:
            logging.error("An error occurred while removing the task.")
            logging.exception(e)
    else:
        logging.warning(f"Task '{task}' not found in the list.")


def clear_all_task():
    user_input = str(
        input(f"Are you sure? Press 'Y' to continue!: ")).strip().upper()
    if user_input == 'Y':
        logging.info(f"Clearing task list started.")
        for task in read_tasks():
            remove_task(task)
        logging.info(f"Clearing task list finished.")

    else:
        logging.info(f"User canceled clearing all tasks.")


def clear_all_tasks_quickly():
    user_input = input("Are you sure? Press 'Y' to continue: ").strip().upper()
    if user_input == 'Y':
    # Itt kilistázzuk hogy mit fogunk törölni csak audit miatt :).
        tasks = read_tasks()
        if len(tasks) == 0:
            logging.info(f"Task list is was empty...there not to much do do here... .  ")
            return
        for task in tasks:
            logging.info(f"Task '{task}' was deleted upon cleaning the task list.")

        try:
            with open(TASK_FILE, "w") as file:
                pass
            logging.info("All tasks cleared successfully.")
        except Exception as e:
                logging.error("An error occurred while clearing tasks.")
                logging.exception(e)
    else:
        logging.info("User canceled clearing all tasks.")


def display_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    print("5. Clear Task List")
    print("6. Clear Task List quickly")


def main():
    while True:
        display_menu()
        choice = input("Choose an option (1, 2, 3, 4, 5 or 6): ")

        if choice == "1":
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == "2":
            tasks = read_tasks()
            if tasks:
                print("\nTasks:")
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")
            else:
                print("No tasks available.")
        elif choice == "3":
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == "4":
            print("Exiting the program.")
            break
        elif choice == "5":
            clear_all_task()
        elif choice == "6":
            clear_all_tasks_quickly()
        else:
            print("Invalid option. Please choose 1, 2, 3, 4 or 5.")


if __name__ == "__main__":
    main()
