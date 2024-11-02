"""
This program creates a todo list where the user can add, read, and remove tasks.
It includes error handling to manage invalid inputs and missing files effectively,
as well as logging to track program activity and errors both in the console and a log file.
"""



#  Logging
import logging

# HANDLER: where the log message should be written/output
# FORMATTER: what should appear in the log message
# Add the FORMATTER to the HANDLER, and then add the HANDLER to the LOGGER

file_handler = logging.FileHandler("app.log") # Write the log to the app.log file
stream_handler = logging.StreamHandler() # Display the log on terminal

# What message is written or displayed in the file or in the terminal
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')  

# Add formatter to the handler
file_handler.setFormatter(formatter) # file_handler uses the same formatter content as stream_handler
stream_handler.setFormatter(formatter)# That said, the same messages display in the file or in the terminal

# Define the logger, add the handler to the logger, and set the level of the logger
logger = logging.getLogger() # Define the logger
logger.addHandler(file_handler) # Add the handler to the logger
logger.addHandler(stream_handler) # Add the handler to the logger
logger.setLevel(logging.DEBUG) # Set the minimum level of the logger (DEBUG is the highest)

# *Functions to add, display, and delete the tasks provided by the user
def add_task():
    # This function allows the user to add a new task.
    # It opens the task file in append mode, adds the task entered by the user,
    # and closes the file, ensuring all previous tasks remain intact.

    with open(
        "python_hu/homeworks/zsoltcsengeri/4_exceptions_logging/tasks.txt", "a"
    ) as file:

        task = input("Enter the task you want to add: ")  # Ask the user for the task

        file.write(task + "\n")  # Write the task to the file with a newline at the end
        logger.info(f"Task '{task}' added to the list.\n")
        # print(f"Task '{task}' added to the list.") * this has now been obsolete due to the log message


def read_task():
    # This function reads and displays all tasks from the task file.
    # It opens the file in read mode, reads all lines, and prints them one by one.
    # The .strip() method is used to remove any trailing newline characters.
    try:
        with open(
            "python_hu/homeworks/zsoltcsengeri/4_exceptions_logging/tasks.txt", "r"
        ) as file:

            lines = file.readlines()
            for line in lines:
                print(line.strip())
    except FileNotFoundError as e:
        logger.error(f"The file not found: {e}\n")
        # print(f"The file not found: {e}") * this has now been obsolete due to the log message


def delete_task():
    # This function allows the user to delete a task from the list.
    # It reads the task file into a list, displays the tasks with their respective IDs,
    # and lets the user select which task to delete by its ID.
    # After deletion, the updated list of tasks is written back to the file.
    try:
        with open(
            "python_hu/homeworks/zsoltcsengeri/4_exceptions_logging/tasks.txt", "r"
        ) as file:
            lines = file.readlines()
        for id, line in enumerate(lines, 1):  # Enumerate the tasks in the list
            print(f"{id} - {line}")
    except FileNotFoundError as e:
        logger.error(f"The file not found: {e}\n")
        # print(f"The file not found: {e}") * this has now been obsolete due to the log message
    
    # *Let the user choose which task to delete

    while True:
        try:
            task_to_delete = int(
                input(
                    "Please provide the id of the task you want to delete from the task list: "
                )
            )

            if task_to_delete < 1 or task_to_delete > len(lines):
                logger.warning(f"Invalid task ID: {task_to_delete}\n")
                #print("The ID you've provided doesn't exist, please give the ID of the task from the list\n") * 
                # this has now been obsolete due to the log file
                continue
            else:
                del lines[
                    task_to_delete - 1
                ]  # The task is deleted by removing the item from the 'lines' list using the index (task_to_delete - 1)
                logger.info(f"Task {task_to_delete} deleted.")
            break
        except ValueError as e:
            logger.error(f"Invalid input: {e}\n")
            # print(f"This error is because {e}: Please enter a number!\n") * this has now been obsolete due to the log file
        continue

    # Need to rewrite the file with the updated list of tasks
    with open(
        "python_hu/homeworks/zsoltcsengeri/4_exceptions_logging/tasks.txt", "w"
    ) as file:
        file.writelines(
            lines
        )  # Writes the remaining tasks (after deletion) back into the task file.


def display_menu():
    # This function continuously displays the menu and prompts the user for input.
    # Based on the user's choice, it calls the appropriate function (add, read, delete, or exit).

    while True:  # Keep showing the menu until the user chooses to exit
        # Display menu options and get input from the user
        try:
            menu = int(
                input(
                    "Please choose an option:\n"
                    "1 - Add a task\n"
                    "2 - View tasks\n"
                    "3 - Delete a task\n"
                    "4 - Exit\n"
                    "Enter your choice: "
                )
            )

            # Handle each option based on the user's input
            if menu == 1:
                add_task()  # Call the add_task() function
            elif menu == 2:
                read_task()  # Call the read_task() function
            elif menu == 3:
                delete_task()  # Call the delete_task() function
            elif menu == 4:
                print("Exiting program...")
                break  # Exit the loop and stop the program
            else:
                print(
                    "Invalid input. Please enter 1, 2, 3, or 4."
                )  # Handle invalid input

        except ValueError as e:
            logger.error(f"Invalid input: {e}\n")
            print(
                f"This error is because {e}: Please enter a number!\n"
            )  # Keep looping if input is not a number


display_menu()
