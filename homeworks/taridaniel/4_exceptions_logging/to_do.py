import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('app.log'), logging.StreamHandler()])

# Create an empty .txt file
open('tasks.txt', 'w').close()

def read_tasks():
    try:
        with open('taridaniel/4_exceptions_logging/tasks.txt', 'r') as file:
            tasks = file.readlines()
            if not tasks:
                logging.info("No tasks found.")
            return [task.strip() for task in tasks]
    except Exception as e:
        logging.error(f"Error reading tasks: {e}")
        return []

def add_task(task):
    try:
        with open('taridaniel/4_exceptions_logging/tasks.txt', 'a') as file:
            file.write(f"{task}\n")
        logging.info(f"Task '{task}' added.")
    except Exception as e:
        logging.error(f"Error adding task: {e}")

def remove_task(task):
    try:
        tasks = read_tasks()
        if task in tasks:
            tasks.remove(task)
            with open('/taridaniel/4_exceptions_logging/tasks.txt', 'w') as file:
                for t in tasks:
                    file.write(f"{t}\n")
            logging.info(f"Task '{task}' removed.")
        else:
            logging.warning(f"Task '{task}' not found.")
    except Exception as e:
        logging.error(f"Error removing task: {e}")

def display_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                task = input("Enter the task to add: ")
                add_task(task)
            elif choice == 2:
                tasks = read_tasks()
                if tasks:
                    for i, task in enumerate(tasks, 1):
                        print(f"{i}. {task}")
                else:
                    print("No tasks to display.")
            elif choice == 3:
                task = input("Enter the task to remove: ")
                remove_task(task)
            elif choice == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            logging.error("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
