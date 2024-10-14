

def add_task():
    # Open the file in append mode ("a") so that tasks are added without overwriting existing ones
    with open("python_hu/homeworks/zsoltcsengeri/4_exceptions_logging/tasks.txt", "a") as file:
        task = input("Enter the task you want to add: ")  # Ask the user for the task
        file.write(task + "\n")  # Write the task to the file with a newline at the end
        print(f"Task '{task}' added to the list.")

def read_task():
    # Placeholder for reading tasks logic
    pass

def delete_task():
    # Placeholder for deleting task logic
    pass

def display_menu():
    while True:  # Keep showing the menu until the user chooses to exit
        # Display menu options and get input from the user
        menu = int(input("Please enter 1 for adding, 2 for reading, 3 for deleting, or 4 for exiting: "))
        
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
