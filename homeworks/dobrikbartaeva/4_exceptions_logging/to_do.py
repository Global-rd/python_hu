import os
import logging
to_do_list_path = "homeworks/dobrikbartaeva/4_exceptions_logging/to_do_list.txt"
def setup_logger(logger_name, log_file="homeworks/dobrikbartaeva/4_exceptions_logging/app.log",level=logging.INFO):
    logger = logging.getLogger(logger_name)                                         #Call getlogger function from logging module
    file_handler = logging.FileHandler(log_file)                                    #Where we write the log messages
    stream_handler = logging.StreamHandler()  
                                            #Where we write the log messages
    #Format of the messages:
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    #Assign formatter to the handler:
    file_handler.setFormatter(formatter)                                            
    stream_handler.setFormatter(formatter)   

    #Assign the level of the message to the handler 
    file_handler.setLevel(logging.DEBUG)                                            
    stream_handler.setLevel(logging.DEBUG)  

    #Add handler to the logger:
    logger.addHandler(file_handler)                                                 
    logger.addHandler(stream_handler)                                               
    logger.setLevel(level)                                                          
    return logger

logger = setup_logger("to_do_logger")

with open(to_do_list_path, "w") as file:
    file.write("")

def add_task(task_input):
    with open(to_do_list_path, "a") as file:
        file.write(f"{task_input}\n")
        logger.info(f"You added: {task_input}")
    return True

def view_tasks():
    with open(to_do_list_path, "r") as file:
        lines = file.readlines()
    if not lines:
        logger.info("To do list is empty.")
    else:
        logger.info("To do list:")   
        for id, line in enumerate(lines,1):
            logger.info(f"{id}. - {line.strip()}")
    return True

def remove_task(task_input):
    with open(to_do_list_path, "r") as file:
        lines = file.readlines()
    new_lines = [line for line in lines if line.strip() != task_input]
    if len(new_lines) == len(lines):
        logger.info(f"This task is not on your to do list: {task_input}")
    else:
        with open(to_do_list_path, "w") as file:
            file.writelines(new_lines)
        logger.info(f"You removed: {task_input}")
    return True

def exit_file():
    logger.info("Exiting...")
    return False

action_list = {
    1: ["Add Task", "Enter task to add: ", add_task],
    2: ["View Tasks", "", view_tasks],
    3: ["Remove Task", "Enter task you'd like to remove: ", remove_task],
    4: ["Exit", "", exit_file]
}

def print_choice_options():
    logger.info("Available actions:")
    for key, value in action_list.items():
        print(f"{key}. {value[0]}")
    return True

def user_input():
    while True:
        try:
            action_number = int(input("Choose action from 1 to 4: "))
            if action_number in action_list:
                return action_number
            else:
                logger.info("Number should be between 1 and 4.")
        except ValueError:
            logger.info("Invalid input. Please enter a number.")   

print_choice_options()

running_code=True

while running_code:
    action_number=user_input()
    if action_list[action_number][1] != "":
        task_input= input(f"{action_list[action_number][1]}")
        running_code=action_list[action_number][-1](task_input)
    else:
        running_code=action_list[action_number][-1]()