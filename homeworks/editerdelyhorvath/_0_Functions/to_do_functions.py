'''
Definiciók a to_do file-hoz

'''

from setup_logger_edit import setup_logger
import logging
import shutil  # for moving the temp file to original file

#################### LOGGER SETUP #################### 

# Define a function to set up the logger for to_do_functions.py
def setup_logger_for_functions(log_file_path):
    '''Sets up the logger for to_do_functions using the provided log file path.'''
    global logger
    logger = setup_logger(name='to_do_functions', log_file=log_file_path, level=logging.INFO)

#################### FUNCTIONS #################### 

# Function to read a file line by line
def read_file_line_by_line(file_path):
    '''Reads the file line by line'''
    try:
        with open(file_path, "r") as file:
            for line in file:
                yield line
    except FileNotFoundError as e:
        logger.error(f"File not found: {file_path}. Error: {e}")
        raise

# Function to read and print all lines from a file
def read_your_file_line_by_line(file_path):
    '''This function reads and prints the lines from the file.'''
    try:
        for line in read_file_line_by_line(file_path=file_path):
            print(line.strip())
        print(f"\nAll of the lines in your To_Do list are printed.\n\n")
        logger.info(f"File {file_path} read successfully.")
    except Exception as e:
        logger.error(f"Error reading the file: {e}")

# Function to add a new task (append new line)
def add_new_task(file_path):
    '''Adds a new task (line) to the specified file.'''
    try:
        with open(file_path, 'a') as file:
            task = str(input("Enter the next task: ")).strip()
            file.write(f'{task}\n')
        logger.info(f"Task added: {task}")
    except Exception as e:
        logger.error(f"Error adding a new task: {e}")

# Function to ask whether to keep or delete each line
def ask_to_keep_or_delete_line(line):
    '''Asks the user if they want to keep or delete the given line.''' 
    while True:
        response = input(f"Do you want to delete this line? (yes/no):\n{line.strip()}\n> ").strip().lower()
        if response in ['yes', 'no']:
            logger.info(f"User decided to {'keep' if response == 'no' else 'delete'} the task: {line.strip()}")
            return response == 'no'  # Return True if user wants to keep the line
        print("Invalid response. Please enter 'yes' or 'no'.")

# Process the file, asking for each line
def process_file(file_path, temp_file_path):
    '''Reads the file and asks for each line whether to keep or delete, writes the result to a temporary file.'''
    try:
        with open(file_path, 'r') as original_file, open(temp_file_path, 'w') as temp_file:
            for line in original_file:
                if ask_to_keep_or_delete_line(line):   # Keep the line if user says "no" to deleting
                    temp_file.write(line)

        shutil.move(temp_file_path, file_path)
        logger.info(f"File {file_path} updated successfully.")
        print(f"File has been updated.")
    except Exception as e:
        logger.error(f"Error processing the file: {e}")

# Function to delete a specific task by name
def delete_task_by_name(file_path, task_name):
    '''Deletes a specific task by its name.'''
    try:
        temp_file_path = file_path + '.tmp'
        task_found = False

        with open(file_path, 'r') as original_file, open(temp_file_path, 'w') as temp_file:
            for line in original_file:
                if line.strip() == task_name:
                    task_found = True
                    print(f"Task '{task_name}' has been deleted.")
                    logger.info(f"Task '{task_name}' deleted.")
                else:
                    temp_file.write(line)

        if not task_found:
            print(f"Task '{task_name}' not found in the list.")
            logger.warning(f"Task '{task_name}' not found in {file_path}.")

        shutil.move(temp_file_path, file_path)
    except Exception as e:
        logger.error(f"Error deleting task by name: {e}")

# Function to delete tasks based on user's choice
def delete_task_menu(file_path, temp_file_path):
    '''Offers a menu to delete a task either by name or by going through the list.'''
    print("Would you like to:")
    print("  1. Delete a task by name")
    print("  2. Go through the list and choose which tasks to delete")

    choice = input("Enter 1 or 2: ").strip()
    
    if choice == '1':
        task_name = input("Enter the exact task you want to delete: ").strip()
        delete_task_by_name(file_path, task_name)
    elif choice == '2':
        process_file(file_path, temp_file_path)
    else:
        print("Invalid choice. Returning to main menu.")



