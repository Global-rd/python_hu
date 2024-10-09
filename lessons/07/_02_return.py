#function ami nem ad vissza értéket:
def greet_user(name):
    return f"Hello {name}, welcome home!"


value = greet_user("Alice")
print(value)
print(type(value))


#function amik visszadnak értékeket

def add(num_1: int, num_2: int) -> int:
    return num_1 + num_2


my_number = add(1, 2)
print(my_number)
print(type(my_number))

#function 

#return early

def calculate_age_in_days(age):
    if age < 0:
        print("Invalid age! Please provide a positive number!")
        return 
    age_in_days = age * 365

    return age_in_days


age_in_days = calculate_age_in_days(10)


#returning multiple values

def multiply_two_values(a, b):
    return a*2, b*2

print(type(multiply_two_values(1,2)))

x,y = multiply_two_values(1,2)

