def divide_numbers(a, b):
    return a / b

#ZERO DIVISION ERROR
num = divide_numbers(10, 1) #0-val osztottunk
print(num)

#VALUE ERROR

#age = float(input("How old are you? (please provide a number!)"))
#print(age)

#INDEX ERROR
my_list = [1,2,3,4,5]
print(my_list[0])
#print(my_list[5])


#HANDLING EXCEPTIONS: built in exceptions: https://www.w3schools.com/python/python_ref_exceptions.asp
try:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    c = a / b
except ZeroDivisionError as e:
    print(f"Zero div. error: {e}")
except ValueError as e:
    print(f"Value error: {e}")
except Exception as e:
    print(f"Something unexpected happened: {e}")
else:
    print(c)
finally:
    print("Division attempt finished.")


print("valami")


#RAISE EXCEPTIONS:

#BAD example
def calculate_rectangle_area(a, b):
    return a * b

area = calculate_rectangle_area(10, 5)
area_error = calculate_rectangle_area(10, -1)

#SOLVE ISSUES:
def calculate_rectangle_area(length, width):

    if length <=0 or width <= 0:
        raise ValueError("Both params must be a positive number for the rectangle!")
    
    return length * width


try:
    area = calculate_rectangle_area(5, -1)
except ValueError as e:
    print(f"Value error {e}")
except TypeError as e:
    print(f"Type error: {e}")


# custom exception