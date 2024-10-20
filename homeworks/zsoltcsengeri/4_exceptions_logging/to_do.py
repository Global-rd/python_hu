def add_task():
    # This function allows the user to add a new task.
    # It opens the task file in append mode, adds the task entered by the user,
    # and closes the file, ensuring all previous tasks remain intact.
    with open(
        "python_hu/homeworks/zsoltcsengeri/4_exceptions_logging/tasks.txt", "a"
    ) as file:
        task = input("Enter the task you want to add: ")  # Ask the user for the task
        file.write(task + "\n")  # Write the task to the file with a newline at the end
        print(f"Task '{task}' added to the list.")


def read_task():
    # This function reads and displays all tasks from the task file.
    # It opens the file in read mode, reads all lines, and prints them one by one.
    # The .strip() method is used to remove any trailing newline characters.

    with open(
        "python_hu/homeworks/zsoltcsengeri/4_exceptions_logging/tasks.txt", "r"
    ) as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())


def delete_task():
    # This function allows the user to delete a task from the list.
    # It reads the task file into a list, displays the tasks with their respective IDs,
    # and lets the user select which task to delete by its ID.
    # After deletion, the updated list of tasks is written back to the file.

    with open(
        "python_hu/homeworks/zsoltcsengeri/4_exceptions_logging/tasks.txt", "r"
    ) as file:
        lines = file.readlines()
        for id, line in enumerate(lines, 1):  # Enumerate the tasks in the list
            print(f"{id} - {line}")
    # Let the user choose which task to delete
    task_to_delete = int(
        input("Please provide the id of the task you want to delete from the task list: ")
    )
    del lines[
        task_to_delete - 1
    ]  # The task is deleted by removing the item from the 'lines' list using the index (task_to_delete - 1).

    print(lines)
    # Need to rewrite the file with the updated list of tasks
    with open(
        "python_hu/homeworks/zsoltcsengeri/4_exceptions_logging/tasks.txt", "w"
    ) as file:
        file.writelines(
            lines
        )  # Writes the remaining tasks (after deletion) back into the task file.


def display_menu():
    # This function continuously displays the menu and prompts the user for input.
    # Based on the user's choice, it calls the appropriate function (add, read, delete, or exit).

    while True:  # Keep showing the menu until the user chooses to exit
        # Display menu options and get input from the user
        menu = int(
    input(
        "Please choose an option:\n"
        "1 - Add a task\n"
        "2 - View tasks\n"
        "3 - Delete a task\n"
        "4 - Exit\n"
        "Enter your choice: "
    )
)


        # Handle each option based on the user's input
        if menu == 1:
            add_task()  # Call the add_task() function
        elif menu == 2:
            read_task()  # Call the read_task() function
        elif menu == 3:
            delete_task()  # Call the delete_task() function
        elif menu == 4:
            print("Exiting program...")
            break  # Exit the loop and stop the program
        else:
            print("Invalid input. Please enter 1, 2, 3, or 4.")  # Handle invalid input


display_menu()
