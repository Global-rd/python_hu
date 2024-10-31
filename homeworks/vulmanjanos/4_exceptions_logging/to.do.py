import os
import logging

# Logging setup

log_file = "homeworks/vulmanjanos/4_exceptions_logging/log.log"
file_name = "homeworks/vulmanjanos/4_exceptions_logging/to_do.txt"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler(log_file),
    logging.StreamHandler()
])

#feladat beolvasás
def read_tasks(file_name):
    try:
        with open(file_name, 'r') as file:
            tasks = file.readlines()
        logging.info("Tasks read successfully.")
        return tasks
    except Exception as e:
        logging.error(f"Error reading tasks: {e}")
        return []

#feladat hozzáadás
def add_task(file_name, task):
    try:
        with open(file_name, 'a') as file:
            file.write(task + '\n')
        logging.info("Task added successfully.")
    except Exception as e:
        logging.error(f"Error adding task: {e}")

#feladat törlése
def remove_task(file_name, task):
    try:
        tasks = read_tasks(file_name)
        with open(file_name, 'w') as file:
            for t in tasks:
                if t.strip() != task:
                    file.write(t)
        logging.info("Task removed successfully.")
    except Exception as e:
        logging.error(f"Error removing task: {e}")

#opciók választása
def display_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

#folyamat futtatás, hibaüzenettel
def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            task = input("Enter the task: ")
            add_task(file_name, task)
        elif choice == '2':
            tasks = read_tasks(file_name)
            print("Tasks:")
            for task in tasks:
                print(task.strip())
        elif choice == '3':
            task = input("Enter the task to remove: ")
            remove_task(file_name, task)
        elif choice == '4':
            print("Exiting")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()