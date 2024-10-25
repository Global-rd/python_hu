import logging

# Install logger
def setup_logger(logger_name, log_file="homeworks/zlinszkygyorgy/4_exceptions_logging/app.log", level=logging.INFO):
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)

    # Stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)

    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # Add handler to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger

logger = setup_logger('zgylogger')

# To do list - reading
def read_tasks(file_name):
    try:
        with open(file_name, "r") as file:
            tasks = file.readlines()
        logger.info("To do list read successfully")
        return [task.strip() for task in tasks]
    except Exception as e:
        logger.error(f"Something unexpected happened: {e}")
        return []
    
# Adding tasks
def add_task(file_name, task):
    try:
        with open(file_name, "a") as file:
            file.write(task + "\n")
        logger.info(f"Task added: {task}")
    except Exception as e:
        logger.error(f"Error adding task: {e}")

# Deleting tasks
def remove_task(file_name, task):
    try:
        tasks = read_tasks(file_name)
        if task in tasks:
            tasks.remove(task)
            with open(file_name, "w") as file:
                for t in tasks:
                    file.write(t + "\n")
            logger.info(f"Task removed: {task}")
        else:
            logger.warning(f"Task not found: {task}")
    except Exception as e:
        logger.error(f"Could not remove task: {e}")

# Display menu
def display_menu():
    print("1. Add task")
    print("2. List tasks")
    print("3. Remove task")
    print("4. Exit")

# Main program
def main():
    file_name = "homeworks/zlinszkygyorgy/4_exceptions_logging/to_do_list.txt"
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            task = input("Enter a task to add: ")
            add_task(file_name, task)
        elif choice == "2":
            tasks = read_tasks(file_name)
            print("Tasks:")
            for task in tasks:
                print(f"- {task}")
        elif choice == "3":
            task = input("Enter the task to remove: ")
            remove_task(file_name, task)
        elif choice == "4":
            print("Exiting")
            break
        else:
            print("Invalid choice, please choose a number between 1 and 4.")

main()
