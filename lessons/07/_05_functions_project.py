def register_user(users, name, age):
    """Registers a user to the users list"""
    user = {"name": name, "age": age}
    users.append(user)
    print(f"User registered: {user}")

def update_user_age(users, name, new_age):
    """Updates the users's age based on the given name"""
    for user in users:
        if user["name"] == name:
            user["age"] = new_age
            print(f"User {name}'s age has been updated to {new_age}")
            return
    print(f"No user named {name} is present in the users list")


def display_user_info(users, name):
    """Displays all information of a speficic user"""
    for user in users:
        if user["name"] == name:
            print(f"User info - Name: {user['name']} Age: {user['age']}")


def display_all_users(users):
    """Displays all information for all users"""
    print("Registered users:")
    for id, user in enumerate(users):
        print(f"{id}. - {user['name']} (Age: {user['age']})")


def main():
    users = []
    register_user(users = users, name = "Alice", age = 15)
    register_user(users = users, name = "John", age = 20)
    register_user(users = users, name = "Dexter", age = 30)
    update_user_age(users=users, name="Alice", new_age=20)
    display_all_users(users=users)
    
main()


#[{"name": "Steve",
#  "age": 15},
#  {"name": "Alice",
#  "age": 30}
#]
