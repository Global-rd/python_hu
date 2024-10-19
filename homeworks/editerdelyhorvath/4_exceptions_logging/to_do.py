'''
4. házi feladat

Feladatkezelő alkalmazás készítése
'''


import sys
import os
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../_0_Functions')))

#################### LOGGER SETUP #################### 

from setup_logger_edit import setup_logger
from to_do_functions import setup_logger_for_functions

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



#################### HELPER FUNCTIONS #################### 

from terminal_clearer import clear_terminal
from to_do_functions import read_your_file_line_by_line, add_new_task, delete_task_menu

clear_terminal()
#################### TO_DO.TXT FILE CREATION #################### 

# Define the file path (same directory as the script)
file_path = os.path.join(current_dir, 'to_do.txt')
temp_file_path = os.path.join(current_dir, 'temp_todo.txt')


# Create and open the file for writing
with open(file_path, 'w') as file:
    pass  # Leave the file empty

logger.info(f"Log file created at: {file_path}")


#################### MAIN APPLICATION LOOP #################### 

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

    try: 
        # Ask the user for input
        selected_number = int(input("Please select a task by its number: ").strip())

        # Check if the task is on the list
        if 1 <= selected_number <= len(display_options):
            selected_option = display_options[selected_number - 1]
            logger.info(f"User selected: {selected_option}")
        else:
            raise ValueError(f"The selected number must be between 1 and {len(display_options)}.")
        
        clear_terminal()

        print(f"Selected option: {selected_option}\n")
    
        if selected_number == 1:
            add_new_task(file_path=file_path)
            logger.info("New task added.")
            input("Press Enter to continue...")
        elif selected_number == 2:
            read_your_file_line_by_line(file_path=file_path)
            logger.info("Viewed tasks.")
            input("Press Enter to continue...")
        elif selected_number == 3:
            delete_task_menu(file_path=file_path, temp_file_path=temp_file_path)
            logger.info("Task removal process initiated.")
            input("Press Enter to continue...")
        elif selected_number == 4:
            logger.info("Exiting application.")
            break

    except ValueError as e:
        print(f"Value error {e}")
        input("Press Enter to continue...")
        
print("The program has finished.")



