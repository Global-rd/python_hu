#PARAMETERS

def greet(name): #parameter
    print(f"Hello {name}")

greet("Johny") # Johnny: argument

# positional parameters:

def add(x,y):
    return x+y

result = add(y = 6, x = 5)
result = add(6,5)

#default argument


def greet(name="Guest"):
    print(f"Dear {name}")

greet("Alice")
greet()


#combining positional, default 

def show_book_details(title, author="Test_Writer", year=2024):

    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Year: {year}")

show_book_details("Test Book")
show_book_details("Test Book", "XY")
show_book_details("Test Book", "XY", 1999)


#keyword arguments
print("--------------------------")
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a(n) {animal_type} named {pet_name}")


describe_pet("Max", animal_type="cat")
describe_pet("Max")


#positional only, keyword only:

def power(base, exponent, /, *, precision=None):
    result = base **  exponent
    if precision:
        return round(result, precision)
    return result


print(power(2.3, 3))
print(power(2.3, 3, precision=2))



#MUTABLE OBJECTS AS DEFAULT ARGUMENTS
# WRONG:

def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

print(append_to_list(1))
print(append_to_list(2))
print(append_to_list(3))

#GOOD EXAMPLE:

def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

print(append_to_list(1))
print(append_to_list(2))
print(append_to_list(3))