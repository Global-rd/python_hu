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
    try:
        with open(file_path, "a") as file:
            file.write(f"{add_element}\n")
            logger.info(f"Add elemnt to the task list: {add_element}.")
    except Exception as e:
        logger.error(f"{e}")

# ------------------------ Menü = 2 -> task_list elemeinek listázása -------------------------
def list_tasklist():
    try:    
        with open(file_path, "r") as file:
            file_element = file.readlines()
            list_range = len(file_element)
            if list_range > 0:
                index_number = 1
                for list_element in file_element:
                    print(f"{index_number}: {list_element.strip()}")
                    index_number += 1
            else:
                print("The list is empty!")
            logger.info("List task elements from the file.")      
    except Exception as e:
            logger.error(f"{e}")

# ------------------------ Menü = 3 -> task_list elem törlése -------------------------
def del_element_of_list(del_index):
    del_list = []
    if del_index > 0:
            with open(file_path, "r") as file:
                del_list = file.readlines()                                     # lista létrehozása fájlból
                del_range=len(del_list)                                         # lista hossz ellenőrzéséhez
                while True:
                    if del_range >= del_index:                                  # lista hossz ellenőrzése
                        del del_list[del_index-1]                               # lista elem törlése index szerint 
                        logger.info(f"The {del_index}. element deleted!")       # log bejegyzés a törlésről
                        with open(file_path, "w") as file:                      # file törlése mert piszok a maradt a file végén
                            file.write("")
                        with open(file_path, "a") as file:                      # file újra írása a módosított list alapján
                            for new_list_elem in del_list:
                                file.write(new_list_elem)
                        logger.info(f"New task list writed back to the file.")  # log bejegyzés az új lista kiírásáról
                        print("Selected element removed!")
                        break
                    else:
                        print("The specified element was greater than the length of the list!")
                        logger.info("The selected item number greater then the list of element number!")
                    break
    else:
        print(f"The specified element must be greater than zero!")
        logger.info("The specified element must be greater than zero!")

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
                    del_element_of_list(del_task_index)
                except ValueError as error:
                    logger.error("The specified element was not a number!")
            elif menu_id == 4:    
                print("Exit!")
                break
            else: print("Next step.")
        else: print("Invalid selection!")
    except ValueError as error:
        logger.error("The specified element was not a number!")
    


        
