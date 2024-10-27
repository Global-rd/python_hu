"""
to_do.py --- Asztalos Lajos --- 2024.10.21
setup_logger function by Nagy István Gábor 
"""
import logging
import msvcrt

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

logger = setup_logger("applog", "homeworks/asztaloslajos/4_exceptions_logging/app.log", level=logging.DEBUG)

#task functions
def add_task(task_definition):
    try:
        with open(FILEPATH + FILENAME, "a") as file:
            file.write(f"{task_definition}\n")
    except Exception as e:
        logger.error(e)
    else: logger.info(TXT_WRITE_INFO)

def view_task():
    try:
        with open(FILEPATH + FILENAME, "r") as file:
            tasks = file.readlines()
    except Exception as e:
        logger.error(e)
    else: 
        logger.info(TXT_READ_INFO)
        for id, task in enumerate(tasks, 1):
            print(f"{id} - {task.strip()}")
    
def remove_task(task_id):
    try:
        with open(FILEPATH + FILENAME, "r") as file:
            rows = file.readlines()
            if len(rows) < task_id:
                print("A tartományon belüli elemet kell megadni")
                mf_wait()
                return(False)
            else: 
                rows.pop(task_id - 1)
    except Exception as e:
        logger.error(e)
    else: logger.info(TXT_READ_INFO)
    try:
        with open(FILEPATH + FILENAME, "w") as file:
            file.writelines(rows)
    except Exception as e:
        logger.error(e)
    else: logger.info(TXT_WRITE_INFO)
    return(True)
def display_menu():
    print("###########################################\n")
    print("                 Feladatkezelő\n")
    for id, item in enumerate(MENU, 1):
        print(f" {id} - {item}")
    print("\n###########################################")
#other function 
def mf_wait():
    print("\nA továbblépéshez nyomjon meg egy billentyűt!")
    msvcrt.getch()

while True:
    display_menu()
    try:
        menu_item = int(input("Kérem válasszon:"))
    except Exception:
        print("egész számot kell megadni!")
        mf_wait()
    else:
        if menu_item == 1:
            menu_param = input("Feladat neve:")
            add_task(menu_param)
        elif menu_item == 3:
            while True:
                view_task()
                menu_param = input("A törlendő feladat sorszáma:")
                try:
                    i = int(menu_param)
                except Exception:
                    print("Egész számot kell megadni!")
                    mf_wait()
                    pass
                else: 
                    if remove_task(int(menu_param)):
                        break
                    else: pass
        elif menu_item == 2:
            view_task()
            mf_wait()
        elif menu_item == 4: break
        else: pass

