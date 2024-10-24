import logging
import logging.config
import os


print(os.getcwd())

logging.config.fileConfig(
    r"c:\Users\tabal\OneDrive\ドキュメント\python_hu\homeworks\karolinavalko\4_exceptions_logging\logger_set_up.ini"
)
logger = logging.getLogger("my_logger")

file_path = r"c:\Users\tabal\OneDrive\ドキュメント\python_hu\homeworks\karolinavalko\4_exceptions_logging\to_do.txt"
to_do_list = []
display_menu = ["Add task", "View task", "Remove task", "Exit"]


def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            logger.info("File had been opened in read mode.")
            return file.readlines()
    except:
        logger.error(f"File {file_path} is not found.")


def view_items():
    to_do_list = read_file(file_path)
    print("Current tasks:")
    for number, item in enumerate(to_do_list, 1):
        print(f"{number}. {item.strip()}")
    logger.info("To do list had been viewed.")
    return to_do_list


def write_list(file_path, list):
    with open(file_path, "w") as file:
        file.write("".join(list))


def add_item():
    with open(file_path, "a+") as file:
        new_item = input("Please type what do you want to add:")
        file.write(new_item + "\n")
        logger.info(f"{new_item} has been successfully added to the To Do list.")


def remove_item():
    try:
        to_do_list = view_items()
        to_remove = int(input("Please select task to remove:"))
        del to_do_list[to_remove - 1]
        write_list(file_path, to_do_list)
        logger.info(f"{to_remove} have been successfully removed from the list.")
    except IndexError as e:
        logger.error(f"Index error: {e}")
        print("This item does not exist. Choose another task to be removed")


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
