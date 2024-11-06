def add_task(input):
    print(f"add task: {input}")

def view_tasks():
    print("view tasks")

def remove_task():
    print("add task")

def exit_file():
    print("exit")

action_list = {
    1: ["Add Task", "Enter task to add", add_task],
    2: ["View Tasks", "", view_tasks],
    3: ["Remove Task", "Which task would you like to remove?", remove_task],
    4: ["Exit", "", exit_file]
}

user_choice = int(input("Choice: "))
#print(action_list[user_choice][0])
input = input(f"{action_list[user_choice][1]}")

print(input)
action_list[user_choice][-1](input)