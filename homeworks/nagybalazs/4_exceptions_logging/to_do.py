"""
Készíts egy Feladatkezelő alkalmazást! 
Hozz létre egy .txt file-t és hagyd üresen.
    - Definiálj 3 függvényt a következőkre: feladatok olvasása, egy feladat hozzáadása, egy feladat törlése.
    - Legyen egy display_menu() function-öd is, ami kiprinteli a lehetséges opciókat:
        1, Add Task
        2, View Tasks
        3, Remove Task
        4, Exit
Folyamatosan kérj be inputot a felhasználótól hogy ezek közül a menüpontok közül mit szeretne csinálni, és hívd meg a válaszhoz megfelelő függvényt. 

A felhasználó inputja 1,2,3 vagy 4 kell, hogy legyen, ellenőrizd! Ha az 1-es vagy 3-as opciót választja,
mindkét esetben paramétert kell átadnod a megfelelő függvénynek.“Exit”-re lépjen ki a program.

Használj hibakezelést a file-ba való íráskor és olvasáskor, illetve használd a logging module-t. 
Egyszerre logolj a konzolra és egy .log file-ba. A .txt file legyen része a pull request-nek, de a log file-ok ne! Használd a .gitignore-t!

Extra: Alakítsd át a .txt file-os megoldást úgy, hogy egy json file-t használsz a feladatok trackelésére
"""

import setup_logger

logger = setup_logger.setup_logger("root_logger")

with open("homeworks/nagybalazs/4_exceptions_logging/ToDo_list.txt", "w") as file:
  file.write("")


def display_menu():
    print("\nMENU:")
    print("--------------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


def get_user_choice():
    while True:
        try:
            choice = int(input("\nEnter which number choice: "))
            return choice
        except ValueError as e:
            logger.error(f"ValueError: {e}")
            print(f"ValueError:: {e}")


def main():    
        while True:
            display_menu()
            choice = get_user_choice()
            if choice == 1:
                add_task()
            elif choice == 2:
                view_task()
            elif choice == 3:
                remove_task()
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")


def add_task():
    new_task = input("New Task: ")
    
    try:
        with open("homeworks/nagybalazs/4_exceptions_logging/ToDo_list.txt", "a") as file:
            file.write(f"{new_task}\n")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")


def view_task():
    try:
        with open("homeworks/nagybalazs/4_exceptions_logging/ToDo_list.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("\nThe To Do list is empty.")
            else:    
                print("\n To Do list: ")
                for line in lines:
                    print(line.strip())
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")


def remove_task():
    try:
        with open("homeworks/nagybalazs/4_exceptions_logging/ToDo_list.txt", "r") as file:
            lines = file.readlines()

        while True:
            task_to_remove = input("\nRemoved task: ").strip()
            if any(line.strip() == task_to_remove for line in lines):
                break
            else:
                print("The specified task is not found in the file, try again.")

        remaining_tasks = [line for line in lines if line.strip() != task_to_remove]
        
        with open("homeworks/nagybalazs/4_exceptions_logging/ToDo_list.txt", "w") as file:
            file.writelines(remaining_tasks)

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()