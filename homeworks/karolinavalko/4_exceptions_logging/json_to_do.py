import logging
import logging.config
import os
import json

print(os.getcwd())

logging.config.fileConfig(
    "homeworks\karolinavalko\4_exceptions_logging\logger_set_up.ini"
)
logger = logging.getLogger("my_logger")


def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            if len(to_do_list) == 0:
                print("The list is empty. There is nothing to be read.")
                return []
            logger.info("File had been opened in read mode.")
            return json.load(file)
    except FileNotFoundError as e:
        logger.warning(f"The file {file_path} does not exist, creating one.")
        write_list(file_path, [])
    except Exception as e:
        logger.error(f"The file {file_path} could not be read: {e}.")
    return []


def view_items():
    to_do_list = read_file(file_path)
    for number, item in enumerate(to_do_list, 1):
        print(f"{number}. {item.strip()}")
    logger.info("To do list had been viewed.")
    return to_do_list


def write_list(file_path, list_to_write):
    with open(file_path, "w") as file:
        json.dump(list_to_write, file, indent=2)


def add_item():
    to_do_list = read_file(file_path)
    new_item = input("Please type what do you want to add:")
    to_do_list.append(new_item)
    write_list(file_path, to_do_list)
    logger.info(f"{new_item} has been successfully added to the To Do list.")
    print(f"You added {new_item} to the list.")


def remove_item():
    try:
        to_do_list = view_items()
        if len(to_do_list) == 0:
            print("The list is empty. Please add first an item.")
            return
        to_remove = int(input("Please select task to remove:"))
        del to_do_list[to_remove - 1]
        write_list(file_path, to_do_list)
        logger.info(f"{to_remove} have been successfully removed from the list.")
    except IndexError as e:
        logger.error(f"Index error: {e}")
        print("This item does not exist. Choose another task to be removed")


def main_function():
    while True:
        print("Display Menu")
        for id, option in enumerate(display_menu, 1):
            print(f"{id}. - {option}")

        try:
            menu_id = int(input("Please choose action from the display menu above:"))
        except ValueError as e:
            logger.error(f"Value error: {e}")
            print("Please add a number between 1-4")
        if menu_id == 1:
            add_item()
        elif menu_id == 2:
            view_items()
        elif menu_id == 3:
            remove_item()
        elif menu_id == 4:
            logger.info("User exited the To do list.")
            print("Goodbye!")
            break


file_path = "homeworks/karolinavalko/4_exceptions_logging/to_do.json"
to_do_list = []
display_menu = ["Add task", "View task", "Remove task", "Exit"]
main_function()
