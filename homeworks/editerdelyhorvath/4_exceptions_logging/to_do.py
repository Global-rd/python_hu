'''
4. házi feladat

Feladatkezelő alkalmazás készítése
'''



import sys
import os
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../_0_Functions')))

from setup_logger_edit import setup_logger
from to_do_functions import setup_logger_for_functions

from terminal_clearer import clear_terminal            # helper functions
from to_do_functions import display_tasks, add_new_task, delete_tasks, get_selected_option, is_file_empty

#################### LOGGER SETUP #################### 

# Set up logging to log to both a file and the console
current_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(current_dir, 'logs')
log_file_path = os.path.join(log_dir, 'app.log')  

# Create the logs directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Set up logging to log to both a file and the console
logger = setup_logger(name="to_do.py", log_file=log_file_path, level=logging.INFO)

# Initialize the logger for to_do_functions.py 
setup_logger_for_functions(log_file_path)  


#################### TO_DO.TXT FILE CREATION #################### 

# Define the file path (same directory as the script)
file_path = os.path.join(current_dir, 'to_do.txt')
temp_file_path = os.path.join(current_dir, 'temp_todo.txt')


# Try to create the file
try:
    with open(file_path, 'w') as file:
        pass  # Leave the file empty
    logger.info(f"Log file created at: {file_path}")
except OSError as e:
    logger.error(f"Failed to create log file at {file_path}: {e}")
    raise


#################### MAIN APPLICATION LOOP #################### 

clear_terminal()

display_options = [
    "Add Task",
    "View Tasks",
    "Remove Task(s)",
    "Exit"  
]

while True:
    clear_terminal()
    print(f"For working with your To_Do list select a task: ")
    for id,option in enumerate(display_options,1):
        print(f"  {id} -> {option}")

    
    # Get the user's selection through the get_selected_option function
    selected_number = get_selected_option(display_options)
    selected_option = display_options[selected_number - 1]

    print(f"Selected option: {selected_option}\n")

    try:
        if selected_number == 1:
            add_new_task(file_path=file_path)
            logger.info("New task added.")
            input("Press Enter to continue...")
        elif selected_number == 2:
            display_tasks(file_path=file_path)
            logger.info("Viewed tasks.")
            input("Press Enter to continue...")
        elif selected_number == 3:
            if is_file_empty(file_path):
                print("The file is empty, there are no tasks to delete.")
                logger.info(f"The To_Do file is empty. No tasks to delete.")
                logger.debug(f"The file {file_path} is empty. No tasks to delete.")
                input("Press Enter to continue...")
            else:
                delete_tasks(file_path=file_path, temp_file_path=temp_file_path)
                logger.info("Task removal process initiated.")
                input("Press Enter to continue...")
        elif selected_number == 4:
            logger.info("Exiting application.")
            break
    except FileNotFoundError as e:
        print(f"Error: {e}")
        logger.error(f"File not found: {e}")
    except OSError as e:
        print(f"Error: {e}")
        logger.error(f"OS error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logger.error(f"Unexpected error: {e}")
    

  
        
print("The program has finished.")



