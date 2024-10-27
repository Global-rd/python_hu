import logging
import os

# File paths
log_filename = "homeworks/boroczpeter/4_exceptions_logging/task_manager.log"
filename = "homeworks/boroczpeter/4_exceptions_logging/tasks.txt"

# Logging setup
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create file handler
file_handler = logging.FileHandler(log_filename)
file_handler.setLevel(logging.INFO)

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter with date and time for both handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Add task to the Tasks list function
def add_task(task):
    try:
        existing_tasks = view_tasks()
        if task in existing_tasks:
            logging.warning(f"The task '{task}' is already in the list")
            print(f"The task '{task}' is already in the list")
        else:   
            with open(filename, "a") as file:
                file.write(f"{task}\n")
            logging.info(f"Task added: {task}")
    except Exception as e:
        logging.error(f"Error while adding task: {e}")

# View Tasks list function
def view_tasks():
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                tasks = file.readlines()
            tasks = [task.strip() for task in tasks]
            logging.info(f"Tasks viewed")
            return tasks
        else:
            logging.info("Task file does not exist. Creating an empty file.")
            # Create an empty file if it does not exist
            open(filename, 'w').close()
            logging.info("Tasks viewed")
            return []
    except Exception as e:
        logging.error(f"Error while viewing tasks: {e}")
        return []

# Remove a task from Tasks list function
def remove_task(task):
    try:
        tasks = view_tasks()
        if task in tasks:
            tasks.remove(task)
            with open(filename, 'w') as file:
                for t in tasks:
                    file.write(f"{t}\n")
            logging.info(f"Task removed: {task}")
        else:
            logging.warning(f"Task not found: {task}")
    except Exception as e:
        logging.error(f"Error while removing task: {e}")

# Display menu function
def display_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

# Main function
def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == '2':
            tasks = view_tasks()
            if tasks:
                print("\nTasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("\nNo task found.")
        elif choice == '3':
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == '4':
            print("\nExit")
            break
        else:
            print("Invalid option. Please choose 1-4.")

# Run the main function
if __name__ == "__main__":
    main()