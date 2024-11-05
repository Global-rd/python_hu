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
    file.write("To do list:\n")

def view_tasks():
    with open(to_do_list_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

def add_task():
    with open(to_do_list_path, "a") as file:
        task_add = input("Enter task to be added:")
        file.write(f"{task_add}\n")

def remove_task():
    task = input("Enter the which you would like to remove: ")
    with open(to_do_list_path, "r") as file:
        lines = file.readlines()
    with open(to_do_list_path, "w") as file:
        for line in lines:
            if line.strip() != task:
                file.write(line)

    with open(to_do_list_path, "r") as file:
        lines = file.readlines()
    with open(to_do_list_path, "w") as file:
        for line in lines:
            if line.strip() != task:
                file.write(line)

def exit_file():
    print("Exiting...")
    return False

#arra gondoltam, hogy ifek helyett mi lenne ha egy dictionarybe ágyazott listában tárolnám a meghívandó
#function-öket is, és akkor innen egyben ki is tudnám displayelni a lehetséges opciókat és nem kellenének
#if-ek sem, mert itt végülis hozzá van rendelve mindegyikhez hogy mit is kellene futtatni.
#nem fut le, de remélem csak a meghívást csinálon rosszul... és nem az alap gondolatom rossz :)
#segítenél megtalálni mi lehet a hiba? köszönöm!
action_list = {
    1: ["Add Task", "Enter task to add", add_task],
    2: ["View Tasks", "", view_tasks],
    3: ["Remove Task", "Which task would you like to remove?", remove_task],
    4: ["Exit", "", exit_file]
}

print(type(action_list))

def print_choice_options():
    print("Available actions:")
    for key, value in action_list.items():
        print(f"{key}. {value[0]}")
    while True:
        try:
            action_number = int(input("Choose action from 1 to 4: "))
            if action_number in action_list:
                return action_number
            else:
                print("Invalid choice. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        print(f"{action_number}")
          
def execute_action(action_number):
    action = action_list[action_number][2]
    print(f"{action}")
    return action

while True:
    action_number=print_choice_options()
    execute_action(action_number)

