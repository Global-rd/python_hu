"""
to_do.py --- Asztalos Lajos --- 2024.10.21
setup_logger function by Nagy István Gábor 
"""
import logging

#parameters
MENU = list(["Feladat hozzáadása","Feladatok listázása","Feladat törlése", "Kilépés"])
FILEPATH = "homeworks/asztaloslajos/4_exceptions_logging/"
FILENAME = "tasks.txt"
TXT_READ_INFO ="The tasks have been read from the file"
TXT_WRITE_INFO ="The task has been written to the file"

#functions
#log functions
def create_file_handler(log_file, level):
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)
    return file_handler

def create_stream_handler(level):
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    return stream_handler

def set_formatter(handler):
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s')
    handler.setFormatter(log_format)

def setup_logger(name, log_file="homeworks/asztaloslajos/4_exceptions_logging/app.log", level=logging.INFO, handlers=None):

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if handlers is None:
        handlers = ['file', 'stream']
    
    for handler in handlers:
        if handler == 'file':
            file_handler = create_file_handler(log_file, level)
            set_formatter(file_handler)
            logger.addHandler(file_handler)
        elif handler == 'stream':
            stream_handler = create_stream_handler(level)
            set_formatter(stream_handler)
            logger.addHandler(stream_handler)
    
    return logger

logger = setup_logger("applog", "homeworks/asztaloslajos/4_exceptions_logging/app.log", level="DEBUG")

#task functions
def add_task(param):
    try:
        with open(FILEPATH + FILENAME, "a") as file:
            file.write(f"{param}\n")
    except Exception as e:
        logger.error(e)
    else: logger.info(TXT_WRITE_INFO)

def view_task():
    try:
        with open(FILEPATH + FILENAME, "r") as file:
            tasks = file.readlines()
    except Exception as e:
        logger.error(e)
    else: logger.info(TXT_READ_INFO)
    for id, task in enumerate(tasks, 1):
        print(f"{id} - {task.strip()}")

def remove_task(param):
    try:
        with open(FILEPATH + FILENAME, "r") as file:
            rows = file.readlines()
            rows.pop(param - 1)
    except Exception as e:
        logger.error(e)
    else: logger.info(TXT_READ_INFO)
    try:
        with open(FILEPATH + FILENAME, "w") as file:
            file.writelines(rows)
    except Exception as e:
        logger.error(e)
    else: logger.info(TXT_WRITE_INFO)

def display_menu():
    print("###########################################\n")
    print("                 Feladatkezelő\n")
    for id, item in enumerate(MENU, 1):
        print(f" {id} - {item}")
    print("\n###########################################")


display_menu()

while True:
    try:
        menu_item = int(input("Kérem válasszon:"))
    except Exception:
        print("egész számot kell megadni!")
    else:
        if menu_item in [1,3]:
            while True:
                menu_param = input("paraméter:")
                if menu_item == 1:
                    add_task(menu_param)
                    break
                else:
                    try:
                        i = int(menu_param)
                    except Exception:
                        print("egész számot kell megadni!")
                        pass
                    else: 
                        remove_task(int(menu_param))
                        break
        elif menu_item == 2:
            view_task()
        elif menu_item == 4: break
        else: pass

