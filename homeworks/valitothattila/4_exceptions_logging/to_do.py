import os
import logging

print(os.getcwd())

file_path = "python_hu/homeworks/valitothattila/4_exceptions_logging/to_do.txt"


# ------------------------ Logolás beállítása -------------------------
file_handler = logging.FileHandler("python_hu/homeworks/valitothattila/4_exceptions_logging/app.log")
stream_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

file_handler.setLevel(logging.DEBUG)
stream_handler.setLevel(logging.DEBUG)

logger = logging.getLogger()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

# ------------------------ Függvények -------------------------

# ------------------------ Menü = 1 -> task_list elem hozzáadása  -------------------------
def add_to_tasklist(add_element):
    main_task_list.append(f"{add_element}\n")
    logger.info(f"Add elemnt to the task list: {add_element}.")

# ------------------------ Menü = 2 -> task_list elemeinek listázása -------------------------
def list_tasklist(): 
    task_list = main_task_list
    list_range = len(task_list)
    if list_range > 0:
        index_number = 1
        for list_element in task_list:
            print(f"{index_number}: {list_element.strip()}")
            index_number += 1
    else:
        print("The list is empty!")
    logger.info("List task elements.")      


# ------------------------ Menü = 3 -> task_list elem törlése -------------------------
def del_element_of_list(del_index, del_list):
    if del_index > 0:                                           
        del_range = len(del_list)                                       # lista hossz ellenőrzéséhez
        while True:
            if del_range >= del_index:                                  # lista hossz ellenőrzése
                del del_list[del_index-1]                               # lista elem törlése index szerint 
                logger.info(f"The {del_index}. element deleted!")       # log bejegyzés a törlésről
                break
            else:
                print("The specified element was greater than the length of the list!")
                logger.info("The selected item number greater then the list of element number!")
            break
    else:
        print(f"The specified element must be greater than zero!")
        logger.info("The specified element must be greater than zero!")
    main_task_list = del_list                                            # módosított listát visszaírjuk az eredeti listába
    return main_task_list

# ------------------------ Menü = 4 -> Fájlba írás és kilépés -------------------------
def exit_function(write_task_list):
    try:
        with open(file_path, "w") as file:                      # file törlése mert piszok a maradt a file végén
            file.write("")
        with open(file_path, "a") as file:                      # fájlba írás
            for new_task_list in write_task_list:
                file.write(new_task_list)
        logger.info("Writing the new task list to a file is complete.")
    except Exception as e:
        logger.error(f"{e}")       


# -------------------------- Főprogram kezdete ---------------------------

# --------------------------- Fájl megnyitás -----------------------------
try:
    with open(file_path, "r") as file:                      # Fájl megnyitás                              
        main_task_list = file.readlines()                   # Fájl beolvasása memória listába
except Exception as e:
    logger.error(f"{e}")
    with open(file_path, "w") as file:                      # Fájl nyitási hiba miatt létrehozunk egy üres fájlt.
        file.write("")
    with open(file_path, "r") as file:                      # Fájl megnyitás
        main_task_list = file.readlines()                   # Fájl beolvasása memória listába

print("Task Managger menu: Add Task(1); View Task(2); Remove Task(3); Exit(4)")

# ------------------------ Menü választás működtetése: -------------------------
while True: 
    try:
        menu_id = int(input("Please choose from the menus(1-4): "))
        if menu_id > 0 and menu_id <= 4:
            #print(f"Thanks for the answer({menu_id})")
            if menu_id == 1:
                #print("------------------- Add task -------------------")
                add_elem = input("Write the new task: ")
                add_to_tasklist(add_elem)
            elif menu_id == 2:
                #print("------------------- List tasks -------------------")
                list_tasklist()
            elif menu_id == 3:    
                #print("------------------- Delete task: -------------------")
                try:
                    del_task_index = int(input("Enter the number of the element to be deleted: "))
                    del_element_of_list(del_task_index, main_task_list)
                except ValueError as error:
                    logger.error("The specified element was not a number!")
            elif menu_id == 4:    
                #print("------------------- Fájlba írás és kilépés -------------------")
                exit_function(main_task_list)
                print("Exit!")
                break
            else: print("Next step.")
        else: print("Invalid selection!")
    except ValueError as error:        
        logger.error("The specified element was not a number!")
    


        
