import logging
import os

# Configure logging to write to both console and a log file
logging.basicConfig(filename='python_hu/homeworks/franktoth/4_exceptions_logging/todo.log', level=logging.INFO, format='%(asctime)s - %(message)s')

#Reads tasks from a file.
def read_tasks(filename):

    try:
        with open(filename, 'r') as f:
            tasks = f.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        logging.error("File not found.")
        return []
    except Exception as e:
        logging.error(f"Error reading file: {e}")
        return []

#Adds a task to the file.
def add_task(filename, task):

    try:
        with open(filename, 'a') as f:
            f.write(task + '\n')
        logging.info(f"Task added: {task}")
    except Exception as e:
        logging.error(f"Error writing to file: {e}")

#Removes a task from the file by index.
def remove_task(filename, task_index):

    try:
        tasks = read_tasks(filename)
        del tasks[task_index]
        with open(filename, 'w') as f:
            for task in tasks:
                f.write(task + '\n')
        logging.info(f"Task removed: {task_index}")
    except IndexError:
        logging.error("No task with that index.")
    except Exception as e:
        logging.error(f"Error removing task: {e}")

#Display the Task Manager menu
def display_menu():
    print("Task Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

filename = "tasks.txt"

#The Task Manager script
def main():
    filename = "tasks.txt"
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        try:
            choice = int(choice)
            if choice == 1:
                task = input("Enter the task: ")
                add_task(filename, task)
            elif choice == 2:
                tasks = read_tasks(filename)
                if tasks:
                    for i, task in enumerate(tasks):
                        print(f"{i+1}. {task}")
                else:
                    print("No tasks found.")
            elif choice == 3:
                tasks = read_tasks(filename)
                if tasks:
                    for i, task in enumerate(tasks):
                        print(f"{i+1}. {task}")
                    index = int(input("Enter the task number to remove: ")) - 1
                    remove_task(filename, index)
                else:
                    print("No tasks to remove.")
            elif choice == 4:
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()